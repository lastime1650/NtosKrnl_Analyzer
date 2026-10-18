# Feature_Sx_PEP_Notification_Synchronization__private_ReportUsage

- RVA: `0x005CF03C`–`0x005CF06E` (길이 `50` bytes)
- VA: `0x00000001405CF03C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085914`
- 디코드: `13`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CF063` → [Feature_Sx_PEP_Notification_Synchronization__private_ReportUsageFallback](Feature_Sx_PEP_Notification_Synchronization__private_ReportUsageFallback_function_005CF074.md) (function, `0x005CF074`)

### Direct callers
- [PoFxInitPowerManagement](../../init/C3/PoFxInitPowerManagement_function_00C3E83C.md) at `0x00C3E842`

### Static image references
- `0x005CF04B` → RVA `0x00FC4760` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CF03C  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
005CF041  48 83 EC 28                     sub rsp, 0x28
005CF045  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
005CF04B  8B 05 0F 57 9F 00               mov eax, dword ptr [rip + 0x9f570f]
005CF051  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005CF055  A8 10                           test al, 0x10
005CF057  75 0F                           jne 0x1405cf068
005CF059  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
005CF05E  BA 03 00 00 00                  mov edx, 3
005CF063  E8 0C 00 00 00                  call 0x1405cf074
005CF068  48 83 C4 28                     add rsp, 0x28
005CF06C  C3                              ret
005CF06D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Sx_PEP_Notification_Synchronization__private_ReportUsage(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (40);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10442511)));
    result = (unsigned int)(*(unsigned int *)(v_rip + 10442511));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10442511)))) & (16)) == 0) {
        a1 = v_stack_p10;
        a2 = 3;
        result = Feature_Sx_PEP_Notification_Synchronization__private_ReportUsageFallback(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Sx_PEP_Notification_Synchronization__private_ReportUsage(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (40);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F570F)));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x9F570F));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F570F)))) & (16)) == 0) {
        Arg1 = v_stack_p10;
        Arg2 = 3;
        result = Feature_Sx_PEP_Notification_Synchronization__private_ReportUsageFallback(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CF03C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CF03C[BB_005CF03C]
  bb_005CF059[BB_005CF059]
  bb_005CF068[BB_005CF068]
  bb_005CF06D[BB_005CF06D]
  bb_005CF03C -->|branch| bb_005CF068
  bb_005CF03C -->|fallthrough| bb_005CF059
  bb_005CF059 -->|flow| bb_005CF068
```
