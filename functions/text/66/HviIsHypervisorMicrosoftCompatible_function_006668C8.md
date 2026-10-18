# HviIsHypervisorMicrosoftCompatible

- RVA: `0x006668C8`–`0x0066690B` (길이 `67` bytes)
- VA: `0x00000001406668C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFA7C`
- 디코드: `16`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006668E8` → [HviGetHypervisorInterface](HviGetHypervisorInterface_function_00666678.md) (function, `0x00666678`)
- `0x00666900` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlpTryConfigureInterface](../58/HvlpTryConfigureInterface_function_0058CABC.md) at `0x0058CB00`
- [KiDetectHardwareSpecControlFeatures](../5B/KiDetectHardwareSpecControlFeatures_function_005BEC4C.md) at `0x005BECC0`
- [HviGetEnlightenmentInformation](HviGetEnlightenmentInformation_function_006665E4.md) at `0x006665F1`
- [HviGetHypervisorFeatures](HviGetHypervisorFeatures_function_00666630.md) at `0x0066663D`
- [HviGetHypervisorVersion](HviGetHypervisorVersion_function_006666C0.md) at `0x006666CD`
- [HviGetImplementationLimits](HviGetImplementationLimits_function_00666708.md) at `0x00666715`
- [HviGetIptFeatures](HviGetIptFeatures_function_006667A8.md) at `0x006667D4`
- [HviGetSharedGpaBoundary](HviGetSharedGpaBoundary_function_00666844.md) at `0x00666861`
- [HalpDmaInitializeCvmSupport](../../init/C2/HalpDmaInitializeCvmSupport_function_00C211C4.md) at `0x00C211E6`

### Static image references
- `0x006668CC` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006668C8  48 83 EC 48                     sub rsp, 0x48
006668CC  48 8B 05 6D 3E 7A 00            mov rax, qword ptr [rip + 0x7a3e6d]
006668D3  48 33 C4                        xor rax, rsp
006668D6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006668DB  0F 57 C0                        xorps xmm0, xmm0
006668DE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006668E3  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006668E8  E8 8B FD FF FF                  call 0x140666678
006668ED  81 7C 24 20 48 76 23 31         cmp dword ptr [rsp + 0x20], 0x31237648
006668F5  0F 94 C0                        sete al
006668F8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006668FD  48 33 CC                        xor rcx, rsp
00666900  E8 3B 5D 04 00                  call 0x1406ac640
00666905  48 83 C4 48                     add rsp, 0x48
00666909  C3                              ret
0066690A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HviIsHypervisorMicrosoftCompatible(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = (*(unsigned __int64 *)(v_rip + 8011373)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = HviGetHypervisorInterface(v_stack_m28, a2, a3, a4);
    result = (v_stack_m28 == 0x31237648ULL) ? 1 : 0;
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
void HviIsHypervisorMicrosoftCompatible(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = (*(uint64_t *)(v_rip + 0x7A3E6D)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = HviGetHypervisorInterface(v_stack_m28, a2, a3, a4);
    result = (v_stack_m28 == 0x31237648ULL) ? 1 : 0;
    a1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006668C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006668C8[BB_006668C8]
  bb_0066690A[BB_0066690A]
```
