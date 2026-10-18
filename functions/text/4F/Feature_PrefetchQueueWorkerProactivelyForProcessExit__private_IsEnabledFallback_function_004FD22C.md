# Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback

- RVA: `0x004FD22C`–`0x004FD242` (길이 `22` bytes)
- VA: `0x00000001404FD22C`
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
- `0x004FD237` → [wil_details_IsEnabledFallback](../4D/wil_details_IsEnabledFallback_function_004DAEFC.md) (function, `0x004DAEFC`)

### Direct callers
- [Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledDeviceUsageNoInline](../34/Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledDeviceUsageNoInline_function_0034A690.md) at `0x0034A6BB`

### Static image references
- `0x004FD230` → RVA `0x000DECB8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FD22C  48 83 EC 28                     sub rsp, 0x28
004FD230  4C 8D 05 81 1A BE FF            lea r8, [rip - 0x41e57f]
004FD237  E8 C0 DC FD FF                  call 0x1404daefc
004FD23C  48 83 C4 28                     add rsp, 0x28
004FD240  C3                              ret
004FD241  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = wil_details_IsEnabledFallback(a1, a2, v_rip - 4318591, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = wil_details_IsEnabledFallback(a1, a2, v_rip - 4318591, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FD22C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FD22C[BB_004FD22C]
  bb_004FD241[BB_004FD241]
```
