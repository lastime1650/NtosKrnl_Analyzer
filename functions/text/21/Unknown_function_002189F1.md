# sub_002189F1

- RVA: `0x002189F1`–`0x00218A6D` (길이 `124` bytes)
- VA: `0x00000001402189F1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005EA60`
- 디코드: `35`개 명령, `124/124` bytes 표시
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
  - `0x00218A3D` → [sub_00218694 + 0x71](Unknown_function_00218694.md) (`tail-transfer`)
  - `0x00218A68` → [sub_00218694 + 0x71](Unknown_function_00218694.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002189F1  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
002189F5  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
002189F9  0F B6 46 28                     movzx eax, byte ptr [rsi + 0x28]
002189FD  88 47 28                        mov byte ptr [rdi + 0x28], al
00218A00  0F B6 46 29                     movzx eax, byte ptr [rsi + 0x29]
00218A04  88 47 29                        mov byte ptr [rdi + 0x29], al
00218A07  0F B6 46 2A                     movzx eax, byte ptr [rsi + 0x2a]
00218A0B  88 47 2A                        mov byte ptr [rdi + 0x2a], al
00218A0E  48 8B 0E                        mov rcx, qword ptr [rsi]
00218A11  48 3B CE                        cmp rcx, rsi
00218A14  75 2C                           jne 0x140218a42
00218A16  48 89 7F 08                     mov qword ptr [rdi + 8], rdi
00218A1A  48 89 3F                        mov qword ptr [rdi], rdi
00218A1D  40 88 6F 29                     mov byte ptr [rdi + 0x29], bpl
00218A21  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
00218A25  48 8D 46 10                     lea rax, [rsi + 0x10]
00218A29  48 3B D0                        cmp rdx, rax
00218A2C  48 8D 47 10                     lea rax, [rdi + 0x10]
00218A30  75 24                           jne 0x140218a56
00218A32  48 89 40 08                     mov qword ptr [rax + 8], rax
00218A36  48 89 00                        mov qword ptr [rax], rax
00218A39  40 88 6F 2A                     mov byte ptr [rdi + 0x2a], bpl
00218A3D  E9 C3 FC FF FF                  jmp 0x140218705
00218A42  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00218A46  48 89 0F                        mov qword ptr [rdi], rcx
00218A49  48 89 47 08                     mov qword ptr [rdi + 8], rax
00218A4D  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00218A51  48 89 38                        mov qword ptr [rax], rdi
00218A54  EB CB                           jmp 0x140218a21
00218A56  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00218A5A  48 89 10                        mov qword ptr [rax], rdx
00218A5D  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00218A61  48 89 42 08                     mov qword ptr [rdx + 8], rax
00218A65  48 89 01                        mov qword ptr [rcx], rax
00218A68  E9 98 FC FF FF                  jmp 0x140218705
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002189F1(void)
{
    *(unsigned __int64 *)(v_rdi + 32) = *(unsigned __int64 *)(v_rsi + 32);
    *(unsigned __int8 *)(v_rdi + 40) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 40));
    *(unsigned __int8 *)(v_rdi + 41) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 41));
    *(unsigned __int8 *)(v_rdi + 42) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 42));
    if ((*(unsigned __int64 *)(v_rsi)) != v_rsi) goto loc_00218A42;
    *(unsigned __int64 *)(v_rdi + 8) = v_rdi;
    *(unsigned __int64 *)(v_rdi) = v_rdi;
    *(unsigned __int8 *)(v_rdi + 41) = (unsigned __int8)(v_rbp);
loc_00218A21:
    if ((*(unsigned __int64 *)(v_rsi + 16)) != (v_rsi + 16)) goto loc_00218A56;
    *(unsigned __int64 *)(v_rdi + 16 + 8) = v_rdi + 16;
    *(unsigned __int64 *)(v_rdi + 16) = v_rdi + 16;
    *(unsigned __int8 *)(v_rdi + 42) = (unsigned __int8)(v_rbp);
loc_00218A42:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_rsi);
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_rsi + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8) = v_rdi;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) = v_rdi;
    goto loc_00218A21;
loc_00218A56:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) = *(unsigned __int64 *)(v_rsi + 16);
    *(unsigned __int64 *)(v_rdi + 24) = *(unsigned __int64 *)(v_rsi + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 8) = *(unsigned __int64 *)(v_rsi + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24)) = *(unsigned __int64 *)(v_rsi + 8);
}
```

## 5. (Beta) C Style

```c
void sub_002189F1(void)
{
    *(uint64_t *)(local_rdi + 0x20) = *(uint64_t *)(local_rsi + 0x20);
    *(uint8_t *)(local_rdi + 0x28) = (uint8_t)(*(uint8_t *)(local_rsi + 0x28));
    *(uint8_t *)(local_rdi + 0x29) = (uint8_t)(*(uint8_t *)(local_rsi + 0x29));
    *(uint8_t *)(local_rdi + 0x2A) = (uint8_t)(*(uint8_t *)(local_rsi + 0x2A));
    if ((*(uint64_t *)(local_rsi)) != local_rsi) goto loc_00218A42;
    *(uint64_t *)(local_rdi + 0x8) = local_rdi;
    *(uint64_t *)(local_rdi) = local_rdi;
    *(uint8_t *)(local_rdi + 0x29) = (uint8_t)(local_rbp);
loc_00218A21:
    if ((*(uint64_t *)(local_rsi + 0x10)) != (local_rsi + 16)) goto loc_00218A56;
    *(uint64_t *)(local_rdi + 0x10 + 0x8) = local_rdi + 16;
    *(uint64_t *)(local_rdi + 0x10) = local_rdi + 16;
    *(uint8_t *)(local_rdi + 0x2A) = (uint8_t)(local_rbp);
loc_00218A42:
    *(uint64_t *)(local_rdi) = *(uint64_t *)(local_rsi);
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_rsi + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8) = local_rdi;
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) = local_rdi;
    goto loc_00218A21;
loc_00218A56:
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) = *(uint64_t *)(local_rsi + 0x10);
    *(uint64_t *)(local_rdi + 0x18) = *(uint64_t *)(local_rsi + 0x18);
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x8) = *(uint64_t *)(local_rsi + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x18)) = *(uint64_t *)(local_rsi + 0x8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002189F1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002189F1[BB_002189F1]
  bb_00218A16[BB_00218A16]
  bb_00218A21[BB_00218A21]
  bb_00218A32[BB_00218A32]
  bb_00218A42[BB_00218A42]
  bb_00218A56[BB_00218A56]
  bb_002189F1 -->|branch| bb_00218A42
  bb_002189F1 -->|fallthrough| bb_00218A16
  bb_00218A16 -->|flow| bb_00218A21
  bb_00218A21 -->|branch| bb_00218A56
  bb_00218A21 -->|fallthrough| bb_00218A32
  bb_00218A42 -->|branch| bb_00218A21
```
