# HviGetHypervisorVendorAndMaxFunction

- RVA: `0x004ADB6C`–`0x004ADBAB` (길이 `63` bytes)
- VA: `0x00000001404ADB6C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `22`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004ADB79` → [HviIsAnyHypervisorPresent](HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)

### Direct callers
- [HvlpHvIdentityInfoCallback](../58/HvlpHvIdentityInfoCallback_function_00584560.md) at `0x0058459E`
- [HvlGetSystemPasidCapabilities](../58/HvlGetSystemPasidCapabilities_function_00588520.md) at `0x005885CB`
- [HviGetIptFeatures](../66/HviGetIptFeatures_function_006667A8.md) at `0x006667E4`
- [HvlQueryDetailInfo](../../page/71/HvlQueryDetailInfo_function_00717BDC.md) at `0x00717C4A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004ADB6C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004ADB71  57                              push rdi
004ADB72  48 83 EC 20                     sub rsp, 0x20
004ADB76  48 8B F9                        mov rdi, rcx
004ADB79  E8 D2 00 00 00                  call 0x1404adc50
004ADB7E  33 C9                           xor ecx, ecx
004ADB80  84 C0                           test al, al
004ADB82  74 1E                           je 0x1404adba2
004ADB84  B8 00 00 00 40                  mov eax, 0x40000000
004ADB89  0F A2                           cpuid
004ADB8B  89 07                           mov dword ptr [rdi], eax
004ADB8D  89 5F 04                        mov dword ptr [rdi + 4], ebx
004ADB90  89 4F 08                        mov dword ptr [rdi + 8], ecx
004ADB93  89 57 0C                        mov dword ptr [rdi + 0xc], edx
004ADB96  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004ADB9B  48 83 C4 20                     add rsp, 0x20
004ADB9F  5F                              pop rdi
004ADBA0  C3                              ret
004ADBA1  CC                              int3
004ADBA2  48 89 0F                        mov qword ptr [rdi], rcx
004ADBA5  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
004ADBA9  EB EB                           jmp 0x1404adb96
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HviGetHypervisorVendorAndMaxFunction(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = HviIsAnyHypervisorPresent(a1, a2, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004ADBA2;
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(0x40000000ULL));
    *(unsigned int *)(a1 + 4) = (unsigned int)(v_rbx);
    *(unsigned int *)(a1 + 8) = 0;
    *(unsigned int *)(a1 + 12) = a2;
loc_004ADB96:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0x40000000ULL);
loc_004ADBA2:
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    goto loc_004ADB96;
}
```

## 5. (Beta) C Style

```c
int64_t HviGetHypervisorVendorAndMaxFunction(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = HviIsAnyHypervisorPresent(Arg1, Arg2, a3, a4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_004ADBA2;
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(0x40000000ULL));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(local_rbx);
    *(uint32_t *)(arg1 + 0x8) = 0;
    *(uint32_t *)(arg1 + 0xC) = Arg2;
loc_004ADB96:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0x40000000ULL);
loc_004ADBA2:
    *(uint64_t *)(arg1) = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    goto loc_004ADB96;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0xC` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004ADB6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004ADB6C[BB_004ADB6C]
  bb_004ADB84[BB_004ADB84]
  bb_004ADB96[BB_004ADB96]
  bb_004ADBA1[BB_004ADBA1]
  bb_004ADBA2[BB_004ADBA2]
  bb_004ADB6C -->|branch| bb_004ADBA2
  bb_004ADB6C -->|fallthrough| bb_004ADB84
  bb_004ADB84 -->|flow| bb_004ADB96
  bb_004ADBA1 -->|flow| bb_004ADBA2
  bb_004ADBA2 -->|branch| bb_004ADB96
```
