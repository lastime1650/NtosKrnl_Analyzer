# PnpValidateStringData

- RVA: `0x004B7678`–`0x004B7695` (길이 `29` bytes)
- VA: `0x00000001404B7678`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PnpValidateRegistryString](PnpValidateRegistryString_function_004B763C.md) at `0x004B7658`
- [PiDevCfgQueryResolveValue](../5A/PiDevCfgQueryResolveValue_function_005A801C.md) at `0x005A80A3`
- [PnpValidateRegistryValue](../5A/PnpValidateRegistryValue_function_005A8218.md) at `0x005A8273`
- [PiDevCfgMakeServiceBootStart](../../page/73/PiDevCfgMakeServiceBootStart_function_00733BC8.md) at `0x00733CCC`
- [PiDevCfgQueryObjectProperties](../../page/97/PiDevCfgQueryObjectProperties_function_0097776C.md) at `0x00977AC6`
- [PiDevCfgResolveVariableDeviceProperty](../../page/AA/PiDevCfgResolveVariableDeviceProperty_function_00AA63A0.md) at `0x00AA6707`
- [PiDevCfgResolveMultiSzValue](../../page/AB/PiDevCfgResolveMultiSzValue_function_00AB6894.md) at `0x00AB694C`
- [sub_00B2C5F4](../../page/B2/Unknown_function_00B2C5F4.md) at `0x00B2C738`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7678  45 33 C0                        xor r8d, r8d
004B767B  83 FA 02                        cmp edx, 2
004B767E  72 10                           jb 0x1404b7690
004B7680  8B C2                           mov eax, edx
004B7682  48 D1 E8                        shr rax, 1
004B7685  66 44 39 44 41 FE               cmp word ptr [rcx + rax*2 - 2], r8w
004B768B  75 03                           jne 0x1404b7690
004B768D  41 B0 01                        mov r8b, 1
004B7690  41 8A C0                        mov al, r8b
004B7693  C3                              ret
004B7694  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpValidateStringData(__int64 a1, int a2, int a3)
{
    __int64 result;

    a3 = 0;
    if (a2 < 2) goto loc_004B7690;
    result = ((unsigned int)(a2)) >> (1);
    if ((*(unsigned __int16 *)(a1 + result * 2 - 2)) == 0) {
        a3 = 1;
    }
    return (unsigned __int8)(a3);
}
```

## 5. (Beta) C Style

```c
int64_t PnpValidateStringData(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg3 = 0;
    if (Arg2 < 2) goto loc_004B7690;
    result = ((uint32_t)(Arg2)) >> (1);
    if ((*(uint16_t *)(arg1 + result * 2 - 0x2)) == 0) {
        Arg3 = 1;
    }
    return (uint8_t)(Arg3);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x2 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7678&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7678[BB_004B7678]
  bb_004B7680[BB_004B7680]
  bb_004B768D[BB_004B768D]
  bb_004B7690[BB_004B7690]
  bb_004B7694[BB_004B7694]
  bb_004B7678 -->|branch| bb_004B7690
  bb_004B7678 -->|fallthrough| bb_004B7680
  bb_004B7680 -->|branch| bb_004B7690
  bb_004B7680 -->|fallthrough| bb_004B768D
  bb_004B768D -->|flow| bb_004B7690
```
