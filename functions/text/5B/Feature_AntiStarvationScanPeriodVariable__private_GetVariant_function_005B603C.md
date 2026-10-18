# Feature_AntiStarvationScanPeriodVariable__private_GetVariant

- RVA: `0x005B603C`–`0x005B6076` (길이 `58` bytes)
- VA: `0x00000001405B603C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005B6050` → [wil_details_FeatureStateCache_GetCachedVariantState](../4A/wil_details_FeatureStateCache_GetCachedVariantState_function_004A3F44.md) (function, `0x004A3F44`)
- `0x005B6062` → [wil_details_FeatureReporting_ReportVariantUsageToService](../37/wil_details_FeatureReporting_ReportVariantUsageToService_function_003782F8.md) (function, `0x003782F8`)

### Direct callers
- [KiInitializeAntiStarvationPolicies](../4F/KiInitializeAntiStarvationPolicies_function_004F5B5C.md) at `0x004F5B69`

### Static image references
- `0x005B6042` → RVA `0x000DE008` (`.rdata`; read)
- `0x005B6049` → RVA `0x00FC48D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B603C  40 53                           push rbx
005B603E  48 83 EC 20                     sub rsp, 0x20
005B6042  48 8D 15 BF 7F B2 FF            lea rdx, [rip - 0x4d8041]
005B6049  48 8D 0D 88 E8 A0 00            lea rcx, [rip + 0xa0e888]
005B6050  E8 EF DE EE FF                  call 0x1404a3f44
005B6055  48 8B D0                        mov rdx, rax
005B6058  48 8D 0D A9 7F B2 FF            lea rcx, [rip - 0x4d8057]
005B605F  48 8B D8                        mov rbx, rax
005B6062  E8 91 22 DC FF                  call 0x1403782f8
005B6067  C1 EB 0C                        shr ebx, 0xc
005B606A  83 E3 3F                        and ebx, 0x3f
005B606D  8B C3                           mov eax, ebx
005B606F  48 83 C4 20                     add rsp, 0x20
005B6073  5B                              pop rbx
005B6074  C3                              ret
005B6075  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_AntiStarvationScanPeriodVariable__private_GetVariant(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = wil_details_FeatureStateCache_GetCachedVariantState(v_rip + 10545288, v_rip - 5079105, a3, a4);
    result = wil_details_FeatureReporting_ReportVariantUsageToService(v_rip - 5079127, result, a3, a4);
    v_rbx = (unsigned int)((result) >> (12));
    v_rbx = (unsigned int)((v_rbx) & (63));
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
void Feature_AntiStarvationScanPeriodVariable__private_GetVariant(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = wil_details_FeatureStateCache_GetCachedVariantState(v_rip + 10545288, v_rip - 5079105, a3, a4);
    result = wil_details_FeatureReporting_ReportVariantUsageToService(v_rip - 5079127, result, a3, a4);
    local_rbx = (uint32_t)((result) >> (12));
    local_rbx = (uint32_t)((local_rbx) & (63));
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B603C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B603C[BB_005B603C]
  bb_005B6075[BB_005B6075]
```
