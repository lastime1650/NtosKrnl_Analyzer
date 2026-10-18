# EtwpUpdateKernelGroupsWork

- RVA: `0x00A4F530`–`0x00A4F553` (길이 `35` bytes)
- VA: `0x0000000140A4F530`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4F536` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A4F548` → [EtwpUpdateGlobalGroupMasks](EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) (function, `0x00A4F55C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A4F53B` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4F536` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4F530  48 83 EC 28                     sub rsp, 0x28
00A4F534  33 D2                           xor edx, edx
00A4F536  E8 35 33 13 00                  call 0x140b82870
00A4F53B  48 8B 0D 66 75 57 00            mov rcx, qword ptr [rip + 0x577566]
00A4F542  33 D2                           xor edx, edx
00A4F544  44 8D 42 08                     lea r8d, [rdx + 8]
00A4F548  E8 0F 00 00 00                  call 0x140a4f55c
00A4F54D  48 83 C4 28                     add rsp, 0x28
00A4F551  C3                              ret
00A4F552  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUpdateKernelGroupsWork(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    a2 = 0;
    result = EtwpUpdateGlobalGroupMasks(*(unsigned __int64 *)(v_rip + 5731686), a2, a2 + 8, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUpdateKernelGroupsWork(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = EtwpUpdateGlobalGroupMasks(*(uint64_t *)(v_rip + 0x577566), Arg2, Arg2 + 8, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4F530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4F530[BB_00A4F530]
  bb_00A4F552[BB_00A4F552]
```
