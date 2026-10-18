# MiGetPageFileHigh

- RVA: `0x0041E6F0`–`0x0041E710` (길이 `32` bytes)
- VA: `0x000000014041E6F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiFreeReservationRun](../../page/A4/MiFreeReservationRun_function_00A4AB74.md) at `0x00A4ABA3`

### Static image references
- `0x0041E6F0` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041E6F0  48 8B 05 89 F5 A0 00            mov rax, qword ptr [rip + 0xa0f589]
0041E6F7  48 85 C0                        test rax, rax
0041E6FA  74 0B                           je 0x14041e707
0041E6FC  F6 C1 10                        test cl, 0x10
0041E6FF  75 06                           jne 0x14041e707
0041E701  48 F7 D0                        not rax
0041E704  48 23 C8                        and rcx, rax
0041E707  48 C1 E9 20                     shr rcx, 0x20
0041E70B  48 8B C1                        mov rax, rcx
0041E70E  C3                              ret
0041E70F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetPageFileHigh(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(v_rip + 10548617) == 0) goto loc_0041E707;
    result = *(unsigned __int64 *)(v_rip + 10548617);
    if ((((unsigned __int8)(a1)) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10548617));
        a1 = (a1) & (result);
    }
    a1 = (a1) >> (32);
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetPageFileHigh(int64_t Arg1)
{
    int64_t result;

    if (*(uint64_t *)(v_rip + 0xA0F589) == 0) goto loc_0041E707;
    result = *(uint64_t *)(v_rip + 0xA0F589);
    if ((((uint8_t)(Arg1)) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA0F589));
        Arg1 = (Arg1) & (result);
    }
    Arg1 = (Arg1) >> (32);
    return Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041E6F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041E6F0[BB_0041E6F0]
  bb_0041E6FC[BB_0041E6FC]
  bb_0041E701[BB_0041E701]
  bb_0041E707[BB_0041E707]
  bb_0041E70F[BB_0041E70F]
  bb_0041E6F0 -->|branch| bb_0041E707
  bb_0041E6F0 -->|fallthrough| bb_0041E6FC
  bb_0041E6FC -->|branch| bb_0041E707
  bb_0041E6FC -->|fallthrough| bb_0041E701
  bb_0041E701 -->|flow| bb_0041E707
```
