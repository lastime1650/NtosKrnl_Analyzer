# HsaGrowPasidTable

- RVA: `0x00574640`–`0x0057466F` (길이 `47` bytes)
- VA: `0x0000000140574640`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00574664` → [HsaAllocatePasidTables](HsaAllocatePasidTables_function_005735DC.md) (function, `0x005735DC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00574640  48 83 EC 48                     sub rsp, 0x48
00574644  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
0057464A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0057464F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00574654  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00574658  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0057465C  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00574660  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00574664  E8 73 EF FF FF                  call 0x1405735dc
00574669  48 83 C4 48                     add rsp, 0x48
0057466D  C3                              ret
0057466E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HsaGrowPasidTable(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = v_stack_p10;
    v_stack_m20 = (unsigned int)((unsigned int)(a6));
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = HsaAllocatePasidTables(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HsaGrowPasidTable(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = v_stack_p10;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = HsaAllocatePasidTables(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00574640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00574640[BB_00574640]
  bb_0057466E[BB_0057466E]
```
