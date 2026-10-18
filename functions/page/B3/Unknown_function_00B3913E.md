# sub_00B3913E

- RVA: `0x00B3913E`–`0x00B39157` (길이 `25` bytes)
- VA: `0x0000000140B3913E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC2B8`
- 디코드: `6`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B3914C` → [PnpLogEvent](../72/PnpLogEvent_function_0072C8FC.md) (function, `0x0072C8FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B39152` → [PnpFixupID + 0x11C](../A2/PnpFixupID_function_00A2B36C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3913E  41 B8 38 00 04 C0               mov r8d, 0xc0040038
00B39144  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B39148  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00B3914C  E8 AB 37 BF FF                  call 0x14072c8fc
00B39151  90                              nop
00B39152  E9 31 23 EF FF                  jmp 0x140a2b488
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B3913E(void)
{
    __int64 result;

    *(unsigned __int64 *)(v_rbp - 8) = result;
    result = PnpLogEvent(a1, v_rbp - 16, (unsigned int)(0xC0040038ULL), a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B3913E(void)
{
    int64_t result;

    *(uint64_t *)(local_rbp - 0x8) = result;
    result = PnpLogEvent(a1, local_rbp - 16, (uint32_t)(0xC0040038ULL), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3913E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B3913E[BB_00B3913E]
```
