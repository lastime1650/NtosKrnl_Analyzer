# sub_00445940

- RVA: `0x00445940`–`0x00445962` (길이 `34` bytes)
- VA: `0x0000000140445940`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5998`
- 디코드: `10`개 명령, `34/34` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00445957` → [sub_004458DF + 0x25](Unknown_function_004458DF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00445940  B8 01 00 00 00                  mov eax, 1
00445945  F0 48 0F C1 43 20               lock xadd qword ptr [rbx + 0x20], rax
0044594B  48 FF C0                        inc rax
0044594E  48 83 F8 01                     cmp rax, 1
00445952  7E 05                           jle 0x140445959
00445954  48 89 1F                        mov qword ptr [rdi], rbx
00445957  EB AB                           jmp 0x140445904
00445959  B9 0E 00 00 00                  mov ecx, 0xe
0044595E  CD 29                           int 0x29
00445960  EB F2                           jmp 0x140445954
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00445940(void)
{
    __int64 result;

    result = (1) + 1;
    if (result <= 1) goto loc_00445959;
loc_00445954:
    *(unsigned __int64 *)(v_rdi) = v_rbx;
loc_00445959:
    goto loc_00445954;
}
```

## 5. (Beta) C Style

```c
void sub_00445940(void)
{
    int64_t result;

    result = (1) + 1;
    if (result <= 1) goto loc_00445959;
loc_00445954:
    *(uint64_t *)(local_rdi) = local_rbx;
loc_00445959:
    goto loc_00445954;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00445940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00445940[BB_00445940]
  bb_00445954[BB_00445954]
  bb_00445959[BB_00445959]
  bb_00445940 -->|branch| bb_00445959
  bb_00445940 -->|fallthrough| bb_00445954
  bb_00445959 -->|branch| bb_00445954
```
