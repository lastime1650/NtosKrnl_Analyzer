# MiSetPageFileAllocationBits

- RVA: `0x003E1D8C`–`0x003E1DBD` (길이 `49` bytes)
- VA: `0x00000001403E1D8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E1DA4` → [RtlSetBits](RtlSetBits_function_003E1610.md) (function, `0x003E1610`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x003733AD`
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x003734B1`
- [MiFindPageFileWriteCluster](MiFindPageFileWriteCluster_function_003E2B00.md) at `0x003E2C1A`
- [MiFindFreePageFileSpace](MiFindFreePageFileSpace_function_003E2CAC.md) at `0x003E2FCA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E1D8C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003E1D91  57                              push rdi
003E1D92  48 83 EC 20                     sub rsp, 0x20
003E1D96  48 8B D9                        mov rbx, rcx
003E1D99  41 8B F8                        mov edi, r8d
003E1D9C  48 8B 49 50                     mov rcx, qword ptr [rcx + 0x50]
003E1DA0  48 83 C1 08                     add rcx, 8
003E1DA4  E8 67 F8 FF FF                  call 0x1403e1610
003E1DA9  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
003E1DAC  2B C7                           sub eax, edi
003E1DAE  89 43 0C                        mov dword ptr [rbx + 0xc], eax
003E1DB1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003E1DB6  48 83 C4 20                     add rsp, 0x20
003E1DBA  5F                              pop rdi
003E1DBB  C3                              ret
003E1DBC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetPageFileAllocationBits(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = (*(unsigned __int64 *)(a1 + 80)) + (8);
    result = RtlSetBits(a1, a2, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) - ((unsigned int)((unsigned int)(a3))));
    *(unsigned int *)(a1 + 12) = (unsigned int)(result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetPageFileAllocationBits(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = (*(uint64_t *)(arg1 + 0x50)) + (8);
    result = RtlSetBits(Arg1, Arg2, Arg3, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) - ((uint32_t)((uint32_t)(Arg3))));
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E1D8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E1D8C[BB_003E1D8C]
  bb_003E1DBC[BB_003E1DBC]
```
