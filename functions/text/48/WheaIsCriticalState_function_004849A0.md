# WheaIsCriticalState

- RVA: `0x004849A0`–`0x004849C2` (길이 `34` bytes)
- VA: `0x00000001404849A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A88`
- 디코드: `12`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004849A4` → [KeGetEffectiveIrql](../2F/KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)

### Direct callers
- [WheapGenerateETWEvents](WheapGenerateETWEvents_function_0048494C.md) at `0x00484955`
- [WheaReportHwError](../4E/WheaReportHwError_function_004ED200.md) at `0x004ED437`
- [WheaReportHwError](../4E/WheaReportHwError_function_004ED200.md) at `0x004ED574`
- [WheaLogInternalEvent](../66/WheaLogInternalEvent_function_006605B0.md) at `0x006606EA`

### Static image references
- `0x004849B5` → RVA `0x00EEF050` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004849A0  48 83 EC 28                     sub rsp, 0x28
004849A4  E8 87 36 E7 FF                  call 0x1402f8030
004849A9  3C 02                           cmp al, 2
004849AB  73 08                           jae 0x1404849b5
004849AD  32 C0                           xor al, al
004849AF  48 83 C4 28                     add rsp, 0x28
004849B3  C3                              ret
004849B4  CC                              int3
004849B5  8B 05 95 A6 A6 00               mov eax, dword ptr [rip + 0xa6a695]
004849BB  85 C0                           test eax, eax
004849BD  0F 9F C0                        setg al
004849C0  EB ED                           jmp 0x1404849af
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaIsCriticalState(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeGetEffectiveIrql(a1, a2, a3, a4);
    if (((unsigned __int8)(result)) >= 2) goto loc_004849B5;
    result = 0;
loc_004849AF:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004849B5:
    result = (condition_is_greater) ? 1 : 0;
    goto loc_004849AF;
}
```

## 5. (Beta) C Style

```c
void WheaIsCriticalState(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeGetEffectiveIrql(a1, a2, a3, a4);
    if (((uint8_t)(result)) >= 2) goto loc_004849B5;
    result = 0;
loc_004849AF:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004849B5:
    result = (condition_is_greater) ? 1 : 0;
    goto loc_004849AF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004849A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004849A0[BB_004849A0]
  bb_004849AD[BB_004849AD]
  bb_004849AF[BB_004849AF]
  bb_004849B4[BB_004849B4]
  bb_004849B5[BB_004849B5]
  bb_004849A0 -->|branch| bb_004849B5
  bb_004849A0 -->|fallthrough| bb_004849AD
  bb_004849AD -->|flow| bb_004849AF
  bb_004849B4 -->|flow| bb_004849B5
  bb_004849B5 -->|branch| bb_004849AF
```
