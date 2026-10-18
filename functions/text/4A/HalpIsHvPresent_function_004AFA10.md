# HalpIsHvPresent

- RVA: `0x004AFA10`–`0x004AFAA3` (길이 `147` bytes)
- VA: `0x00000001404AFA10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8838`
- 디코드: `41`개 명령, `147/147` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004AFA97` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpArtAvailable](HalpArtAvailable_function_004AF870.md) at `0x004AF91D`
- [HalpIsMicrosoftCompatibleHvLoaded](HalpIsMicrosoftCompatibleHvLoaded_function_004AFAAC.md) at `0x004AFAC3`
- [HalpTimerFindIdealPerformanceCounterSource](../53/HalpTimerFindIdealPerformanceCounterSource_function_0053C880.md) at `0x0053C8A6`
- [HalpTimerFindIdealPerformanceCounterSource](../53/HalpTimerFindIdealPerformanceCounterSource_function_0053C880.md) at `0x0053C995`
- [HalDmaAllocateCrashDumpRegistersEx](../53/HalDmaAllocateCrashDumpRegistersEx_function_0053F6D0.md) at `0x0053F850`
- [HalpNmiReboot](../55/HalpNmiReboot_function_0055B2D4.md) at `0x0055B39F`
- [HalSocRequestConfigurationData](../56/HalSocRequestConfigurationData_function_00562ADC.md) at `0x00562B90`
- [HalpLbrInitialize](../../pagelk/B6/HalpLbrInitialize_function_00B60F78.md) at `0x00B60FB9`
- [HalpMiscGetParameters](../../init/C1/HalpMiscGetParameters_function_00C1FD30.md) at `0x00C1FF5A`

### Static image references
- `0x004AFA16` → RVA `0x00E0A740` (`.data`; read)
- `0x004AFA25` → RVA `0x00E0A802` (`.data`; read)
- `0x004AFA85` → RVA `0x00E0A802` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AFA10  40 53                           push rbx
004AFA12  48 83 EC 30                     sub rsp, 0x30
004AFA16  48 8B 05 23 AD 95 00            mov rax, qword ptr [rip + 0x95ad23]
004AFA1D  48 33 C4                        xor rax, rsp
004AFA20  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004AFA25  44 8A 05 D6 AD 95 00            mov r8b, byte ptr [rip + 0x95add6]
004AFA2C  41 80 F8 FF                     cmp r8b, 0xff
004AFA30  75 5A                           jne 0x1404afa8c
004AFA32  45 33 C0                        xor r8d, r8d
004AFA35  33 C9                           xor ecx, ecx
004AFA37  0F 57 C0                        xorps xmm0, xmm0
004AFA3A  0F 11 04 24                     movups xmmword ptr [rsp], xmm0
004AFA3E  45 8D 48 01                     lea r9d, [r8 + 1]
004AFA42  41 8B C1                        mov eax, r9d
004AFA45  0F A2                           cpuid
004AFA47  89 04 24                        mov dword ptr [rsp], eax
004AFA4A  89 5C 24 04                     mov dword ptr [rsp + 4], ebx
004AFA4E  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
004AFA52  89 54 24 0C                     mov dword ptr [rsp + 0xc], edx
004AFA56  85 C9                           test ecx, ecx
004AFA58  79 2B                           jns 0x1404afa85
004AFA5A  0F 11 44 24 10                  movups xmmword ptr [rsp + 0x10], xmm0
004AFA5F  33 C9                           xor ecx, ecx
004AFA61  45 0F B6 C0                     movzx r8d, r8b
004AFA65  B8 01 00 00 40                  mov eax, 0x40000001
004AFA6A  0F A2                           cpuid
004AFA6C  3D 58 62 6E 76                  cmp eax, 0x766e6258
004AFA71  89 44 24 10                     mov dword ptr [rsp + 0x10], eax
004AFA75  89 5C 24 14                     mov dword ptr [rsp + 0x14], ebx
004AFA79  45 0F 45 C1                     cmovne r8d, r9d
004AFA7D  89 4C 24 18                     mov dword ptr [rsp + 0x18], ecx
004AFA81  89 54 24 1C                     mov dword ptr [rsp + 0x1c], edx
004AFA85  44 88 05 76 AD 95 00            mov byte ptr [rip + 0x95ad76], r8b
004AFA8C  41 8A C0                        mov al, r8b
004AFA8F  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
004AFA94  48 33 CC                        xor rcx, rsp
004AFA97  E8 A4 CB 1F 00                  call 0x1406ac640
004AFA9C  48 83 C4 30                     add rsp, 0x30
004AFAA0  5B                              pop rbx
004AFAA1  C3                              ret
004AFAA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIsHvPresent(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m24;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (48);
    result = (*(unsigned __int64 *)(v_rip + 9809187)) ^ (v_rsp);
    v_stack_m18 = result;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 9809366))) != 255) goto loc_004AFA8C;
    a3 = 0;
    a1 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m38 = (unsigned int)((unsigned int)((unsigned int)(a3 + 1)));
    v_stack_m34 = (unsigned int)(v_rbx);
    v_stack_m30 = 0;
    v_stack_m2C = a2;
    result = (unsigned int)((unsigned int)(a3 + 1));
    if (sign_flag) {
        v_stack_m28 = v_xmm0;
        a1 = 0;
        a3 = 0;
        result = 0x40000001ULL;
        v_stack_m28 = (unsigned int)(result);
        v_stack_m24 = (unsigned int)(v_rbx);
        if (((unsigned int)(result)) != 0x766E6258ULL) { a3 = (unsigned int)(a3 + 1); }
        v_stack_m20 = 0;
        v_stack_m1C = a2;
    }
    *(unsigned __int8 *)(v_rip + 9809270) = (unsigned __int8)(a3);
loc_004AFA8C:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a3 + 1);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIsHvPresent(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m24;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (48);
    result = (*(uint64_t *)(v_rip + 0x95AD23)) ^ (local_rsp);
    v_stack_m18 = result;
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x95ADD6))) != 255) goto loc_004AFA8C;
    a3 = 0;
    Arg1 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m38 = (uint32_t)((uint32_t)((uint32_t)(a3 + 1)));
    v_stack_m34 = (uint32_t)(local_rbx);
    v_stack_m30 = 0;
    v_stack_m2C = Arg2;
    result = (uint32_t)((uint32_t)(a3 + 1));
    if (sign_flag) {
        v_stack_m28 = v_xmm0;
        Arg1 = 0;
        a3 = 0;
        result = 0x40000001ULL;
        v_stack_m28 = (uint32_t)(result);
        v_stack_m24 = (uint32_t)(local_rbx);
        if (((uint32_t)(result)) != 0x766E6258ULL) { a3 = (uint32_t)(a3 + 1); }
        v_stack_m20 = 0;
        v_stack_m1C = Arg2;
    }
    *(uint8_t *)(v_rip + 0x95AD76) = (uint8_t)(a3);
loc_004AFA8C:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a3 + 1);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AFA10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AFA10[BB_004AFA10]
  bb_004AFA32[BB_004AFA32]
  bb_004AFA5A[BB_004AFA5A]
  bb_004AFA85[BB_004AFA85]
  bb_004AFA8C[BB_004AFA8C]
  bb_004AFAA2[BB_004AFAA2]
  bb_004AFA10 -->|branch| bb_004AFA8C
  bb_004AFA10 -->|fallthrough| bb_004AFA32
  bb_004AFA32 -->|branch| bb_004AFA85
  bb_004AFA32 -->|fallthrough| bb_004AFA5A
  bb_004AFA5A -->|flow| bb_004AFA85
  bb_004AFA85 -->|flow| bb_004AFA8C
```
