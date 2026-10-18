# MiResumeFromHibernate

- RVA: `0x00678EC0`–`0x00678ED8` (길이 `24` bytes)
- VA: `0x0000000140678EC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00678ECD` → [MiIterateOverPartitions](../47/MiIterateOverPartitions_function_0047FC14.md) (function, `0x0047FC14`)

### Direct callers
- [MmDuplicateMemory](../../pagelk/B7/MmDuplicateMemory_function_00B74158.md) at `0x00B74453`

### Static image references
- `0x00678EC6` → RVA `0x00678EE0` (`MiResumeMarkPageLists`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00678EC0  48 83 EC 28                     sub rsp, 0x28
00678EC4  8B D1                           mov edx, ecx
00678EC6  48 8D 0D 13 00 00 00            lea rcx, [rip + 0x13]
00678ECD  E8 42 6D E0 FF                  call 0x14047fc14
00678ED2  48 83 C4 28                     add rsp, 0x28
00678ED6  C3                              ret
00678ED7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResumeFromHibernate(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiIterateOverPartitions(v_rip + 19, (unsigned int)(a1), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiResumeFromHibernate(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiIterateOverPartitions(v_rip + 19, (uint32_t)(Arg1), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00678EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00678EC0[BB_00678EC0]
  bb_00678ED7[BB_00678ED7]
```
