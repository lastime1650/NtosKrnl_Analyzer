# KiCustomRecurseRoutine3

- RVA: `0x006BC260`–`0x006BC274` (길이 `20` bytes)
- VA: `0x00000001406BC260`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2E0C`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006BC268` → [KiCustomRecurseRoutine4](KiCustomRecurseRoutine4_function_006BC620.md) (function, `0x006BC620`)

### Direct callers
- [KiCustomRecurseRoutine2](KiCustomRecurseRoutine2_function_006BC0E0.md) at `0x006BC0E8`
- [KiCustomAccessRoutine3](KiCustomAccessRoutine3_function_006BC280.md) at `0x006BC29D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006BC260  48 83 EC 28                     sub rsp, 0x28
006BC264  FF C9                           dec ecx
006BC266  74 05                           je 0x1406bc26d
006BC268  E8 B3 03 00 00                  call 0x1406bc620
006BC26D  8B 02                           mov eax, dword ptr [rdx]
006BC26F  48 83 C4 28                     add rsp, 0x28
006BC273  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCustomRecurseRoutine3(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)((a1) - 1);
    if (!(condition_is_equal)) {
        result = KiCustomRecurseRoutine4(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(a2));
}
```

## 5. (Beta) C Style

```c
int64_t KiCustomRecurseRoutine3(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)((Arg1) - 1);
    if (!(condition_is_equal)) {
        result = KiCustomRecurseRoutine4(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(Arg2));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BC260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006BC260[BB_006BC260]
  bb_006BC268[BB_006BC268]
  bb_006BC26D[BB_006BC26D]
  bb_006BC260 -->|branch| bb_006BC26D
  bb_006BC260 -->|fallthrough| bb_006BC268
  bb_006BC268 -->|flow| bb_006BC26D
```
