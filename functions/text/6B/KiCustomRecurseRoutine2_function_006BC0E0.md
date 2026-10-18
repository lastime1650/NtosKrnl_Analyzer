# KiCustomRecurseRoutine2

- RVA: `0x006BC0E0`–`0x006BC0F4` (길이 `20` bytes)
- VA: `0x00000001406BC0E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2A64`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006BC0E8` → [KiCustomRecurseRoutine3](KiCustomRecurseRoutine3_function_006BC260.md) (function, `0x006BC260`)

### Direct callers
- [KiCustomRecurseRoutine1](KiCustomRecurseRoutine1_function_006BC020.md) at `0x006BC028`
- [KiCustomAccessRoutine2](KiCustomAccessRoutine2_function_006BC100.md) at `0x006BC11D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006BC0E0  48 83 EC 28                     sub rsp, 0x28
006BC0E4  FF C9                           dec ecx
006BC0E6  74 05                           je 0x1406bc0ed
006BC0E8  E8 73 01 00 00                  call 0x1406bc260
006BC0ED  8B 02                           mov eax, dword ptr [rdx]
006BC0EF  48 83 C4 28                     add rsp, 0x28
006BC0F3  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCustomRecurseRoutine2(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)((a1) - 1);
    if (!(condition_is_equal)) {
        result = KiCustomRecurseRoutine3(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(a2));
}
```

## 5. (Beta) C Style

```c
int64_t KiCustomRecurseRoutine2(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)((Arg1) - 1);
    if (!(condition_is_equal)) {
        result = KiCustomRecurseRoutine3(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(Arg2));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BC0E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006BC0E0[BB_006BC0E0]
  bb_006BC0E8[BB_006BC0E8]
  bb_006BC0ED[BB_006BC0ED]
  bb_006BC0E0 -->|branch| bb_006BC0ED
  bb_006BC0E0 -->|fallthrough| bb_006BC0E8
  bb_006BC0E8 -->|flow| bb_006BC0ED
```
