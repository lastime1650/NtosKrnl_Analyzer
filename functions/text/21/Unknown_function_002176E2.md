# sub_002176E2

- RVA: `0x002176E2`–`0x00217761` (길이 `127` bytes)
- VA: `0x00000001402176E2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E614`
- 디코드: `35`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00217731` → [sub_0021736A + 0x7D](Unknown_function_0021736A.md) (`tail-transfer`)
  - `0x0021775C` → [sub_0021736A + 0x7D](Unknown_function_0021736A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002176E2  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
002176E6  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
002176EA  41 0F B6 46 28                  movzx eax, byte ptr [r14 + 0x28]
002176EF  88 47 28                        mov byte ptr [rdi + 0x28], al
002176F2  41 0F B6 46 29                  movzx eax, byte ptr [r14 + 0x29]
002176F7  88 47 29                        mov byte ptr [rdi + 0x29], al
002176FA  41 0F B6 46 2A                  movzx eax, byte ptr [r14 + 0x2a]
002176FF  88 47 2A                        mov byte ptr [rdi + 0x2a], al
00217702  49 8B 0E                        mov rcx, qword ptr [r14]
00217705  49 3B CE                        cmp rcx, r14
00217708  75 2C                           jne 0x140217736
0021770A  48 89 7F 08                     mov qword ptr [rdi + 8], rdi
0021770E  48 89 3F                        mov qword ptr [rdi], rdi
00217711  C6 47 29 00                     mov byte ptr [rdi + 0x29], 0
00217715  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
00217719  49 8D 46 10                     lea rax, [r14 + 0x10]
0021771D  48 3B D0                        cmp rdx, rax
00217720  48 8D 47 10                     lea rax, [rdi + 0x10]
00217724  75 24                           jne 0x14021774a
00217726  48 89 40 08                     mov qword ptr [rax + 8], rax
0021772A  48 89 00                        mov qword ptr [rax], rax
0021772D  C6 47 2A 00                     mov byte ptr [rdi + 0x2a], 0
00217731  E9 B1 FC FF FF                  jmp 0x1402173e7
00217736  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0021773A  48 89 0F                        mov qword ptr [rdi], rcx
0021773D  48 89 47 08                     mov qword ptr [rdi + 8], rax
00217741  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00217745  48 89 38                        mov qword ptr [rax], rdi
00217748  EB CB                           jmp 0x140217715
0021774A  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
0021774E  48 89 10                        mov qword ptr [rax], rdx
00217751  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00217755  48 89 42 08                     mov qword ptr [rdx + 8], rax
00217759  48 89 01                        mov qword ptr [rcx], rax
0021775C  E9 86 FC FF FF                  jmp 0x1402173e7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002176E2(void)
{
    *(unsigned __int64 *)(v_rdi + 32) = *(unsigned __int64 *)(v_r14 + 32);
    *(unsigned __int8 *)(v_rdi + 40) = (unsigned __int8)(*(unsigned __int8 *)(v_r14 + 40));
    *(unsigned __int8 *)(v_rdi + 41) = (unsigned __int8)(*(unsigned __int8 *)(v_r14 + 41));
    *(unsigned __int8 *)(v_rdi + 42) = (unsigned __int8)(*(unsigned __int8 *)(v_r14 + 42));
    if ((*(unsigned __int64 *)(v_r14)) != v_r14) goto loc_00217736;
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = v_rdi;
    *(unsigned __int8 *)(v_rdi + 41) = 0;
loc_00217715:
    if ((*(unsigned __int64 *)(v_r14 + 16)) != (v_r14 + 16)) goto loc_0021774A;
    *(unsigned __int64 *)(v_rdi + 16 + 8) = v_rdi + 16;
    *(unsigned __int64 *)(v_rdi + 16) = v_rdi + 16;
    *(unsigned __int8 *)(v_rdi + 42) = 0;
loc_00217736:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_r14);
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_r14 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14) + 8) = v_rdi;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8)) = v_rdi;
    goto loc_00217715;
loc_0021774A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 8)) = *(unsigned __int64 *)(v_r14 + 16);
    *(unsigned __int64 *)(v_rdi + 24) = *(unsigned __int64 *)(v_r14 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 16) + 8) = *(unsigned __int64 *)(v_r14 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 24)) = *(unsigned __int64 *)(v_r14 + 8);
}
```

## 5. (Beta) C Style

```c
void sub_002176E2(void)
{
    *(uint64_t *)(local_rdi + 0x20) = *(uint64_t *)(local_r14 + 0x20);
    *(uint8_t *)(local_rdi + 0x28) = (uint8_t)(*(uint8_t *)(local_r14 + 0x28));
    *(uint8_t *)(local_rdi + 0x29) = (uint8_t)(*(uint8_t *)(local_r14 + 0x29));
    *(uint8_t *)(local_rdi + 0x2A) = (uint8_t)(*(uint8_t *)(local_r14 + 0x2A));
    if ((*(uint64_t *)(local_r14)) != local_r14) goto loc_00217736;
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = local_rdi;
    *(uint8_t *)(local_rdi + 0x29) = 0;
loc_00217715:
    if ((*(uint64_t *)(local_r14 + 0x10)) != (local_r14 + 16)) goto loc_0021774A;
    *(uint64_t *)(local_rdi + 0x10 + 0x8) = local_rdi + 16;
    *(uint64_t *)(local_rdi + 0x10) = local_rdi + 16;
    *(uint8_t *)(local_rdi + 0x2A) = 0;
loc_00217736:
    *(uint64_t *)(local_rdi) = *(uint64_t *)(local_r14);
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_r14 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r14) + 0x8) = local_rdi;
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x8)) = local_rdi;
    goto loc_00217715;
loc_0021774A:
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x8)) = *(uint64_t *)(local_r14 + 0x10);
    *(uint64_t *)(local_rdi + 0x18) = *(uint64_t *)(local_r14 + 0x18);
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x10) + 0x8) = *(uint64_t *)(local_r14 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x18)) = *(uint64_t *)(local_r14 + 0x8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002176E2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002176E2[BB_002176E2]
  bb_0021770A[BB_0021770A]
  bb_00217715[BB_00217715]
  bb_00217726[BB_00217726]
  bb_00217736[BB_00217736]
  bb_0021774A[BB_0021774A]
  bb_002176E2 -->|branch| bb_00217736
  bb_002176E2 -->|fallthrough| bb_0021770A
  bb_0021770A -->|flow| bb_00217715
  bb_00217715 -->|branch| bb_0021774A
  bb_00217715 -->|fallthrough| bb_00217726
  bb_00217736 -->|branch| bb_00217715
```
