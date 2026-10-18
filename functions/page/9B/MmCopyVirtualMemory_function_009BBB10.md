# MmCopyVirtualMemory

- RVA: `0x009BBB10`–`0x009BBB43` (길이 `51` bytes)
- VA: `0x00000001409BBB10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `12`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009BBB38` → [MiCopyVirtualMemory](MiCopyVirtualMemory_function_009BBB50.md) (function, `0x009BBB50`)

### Direct callers
- [PsQueryProcessCommandLine](../../text/46/PsQueryProcessCommandLine_function_00469810.md) at `0x00469ACC`
- [KiTpWriteUmMemory](../../text/5C/KiTpWriteUmMemory_function_005CACB8.md) at `0x005CAD42`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009BBB10  48 83 EC 48                     sub rsp, 0x48
009BBB14  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
009BBB19  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009BBB21  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009BBB26  8A 44 24 78                     mov al, byte ptr [rsp + 0x78]
009BBB2A  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009BBB2E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009BBB33  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009BBB38  E8 13 00 00 00                  call 0x1409bbb50
009BBB3D  48 83 C4 48                     add rsp, 0x48
009BBB41  C3                              ret
009BBB42  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmCopyVirtualMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a7;
    v_stack_m20 = a6;
    v_stack_m28 = a5;
    result = MiCopyVirtualMemory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmCopyVirtualMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint8_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg7;
    v_stack_m20 = Arg6;
    v_stack_m28 = Arg5;
    result = MiCopyVirtualMemory(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BBB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009BBB10[BB_009BBB10]
  bb_009BBB42[BB_009BBB42]
```
