# PopIsHiberbootSupported

- RVA: `0x00702F8C`–`0x00702FA9` (길이 `29` bytes)
- VA: `0x0000000140702F8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) at `0x00910F5A`
- [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) at `0x00910F9D`
- [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) at `0x00910FE0`
- [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) at `0x00911023`
- [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) at `0x00911086`
- [PopVerifySystemPowerState](../A9/PopVerifySystemPowerState_function_00A9537C.md) at `0x00A95408`
- [sub_00B47610](../B4/Unknown_function_00B47610.md) at `0x00B4768B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00702F8C  32 D2                           xor dl, dl
00702F8E  38 51 06                        cmp byte ptr [rcx + 6], dl
00702F91  74 12                           je 0x140702fa5
00702F93  38 51 08                        cmp byte ptr [rcx + 8], dl
00702F96  41 B8 01 00 00 00               mov r8d, 1
00702F9C  0F B6 C2                        movzx eax, dl
00702F9F  41 0F 45 C0                     cmovne eax, r8d
00702FA3  8A D0                           mov dl, al
00702FA5  8A C2                           mov al, dl
00702FA7  C3                              ret
00702FA8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIsHiberbootSupported(__int64 a1, unsigned __int8 a2)
{
    __int64 result;

    a2 = 0;
    if ((*(unsigned __int8 *)(a1 + 6)) != 0) {
        a3 = 1;
        result = 0;
        if ((*(unsigned __int8 *)(a1 + 8)) != 0) { result = (unsigned int)(a3); }
        a2 = (unsigned __int8)(result);
    }
    return a2;
}
```

## 5. (Beta) C Style

```c
int64_t PopIsHiberbootSupported(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg2 = 0;
    if ((*(uint8_t *)(arg1 + 0x6)) != 0) {
        a3 = 1;
        result = 0;
        if ((*(uint8_t *)(arg1 + 0x8)) != 0) { result = (uint32_t)(a3); }
        Arg2 = (uint8_t)(result);
    }
    return Arg2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x6` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00702F8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00702F8C[BB_00702F8C]
  bb_00702F93[BB_00702F93]
  bb_00702FA5[BB_00702FA5]
  bb_00702FA8[BB_00702FA8]
  bb_00702F8C -->|branch| bb_00702FA5
  bb_00702F8C -->|fallthrough| bb_00702F93
  bb_00702F93 -->|flow| bb_00702FA5
```
