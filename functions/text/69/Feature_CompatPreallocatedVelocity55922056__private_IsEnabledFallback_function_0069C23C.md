# Feature_CompatPreallocatedVelocity55922056__private_IsEnabledFallback

- RVA: `0x0069C23C`–`0x0069C252` (길이 `22` bytes)
- VA: `0x000000014069C23C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0069C247` → [wil_details_IsEnabledFallback](../4D/wil_details_IsEnabledFallback_function_004DAEFC.md) (function, `0x004DAEFC`)

### Direct callers
- [Feature_CompatPreallocatedVelocity55922056__private_IsEnabledDeviceUsageNoInline](Feature_CompatPreallocatedVelocity55922056__private_IsEnabledDeviceUsageNoInline_function_0069C204.md) at `0x0069C22B`

### Static image references
- `0x0069C240` → RVA `0x000E02D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069C23C  48 83 EC 28                     sub rsp, 0x28
0069C240  4C 8D 05 89 40 A4 FF            lea r8, [rip - 0x5bbf77]
0069C247  E8 B0 EC E3 FF                  call 0x1404daefc
0069C24C  48 83 C4 28                     add rsp, 0x28
0069C250  C3                              ret
0069C251  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CompatPreallocatedVelocity55922056__private_IsEnabledFallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = wil_details_IsEnabledFallback(a1, a2, v_rip - 6012791, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CompatPreallocatedVelocity55922056__private_IsEnabledFallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = wil_details_IsEnabledFallback(a1, a2, v_rip - 6012791, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069C23C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069C23C[BB_0069C23C]
  bb_0069C251[BB_0069C251]
```
