# MiDeletePageFileMemoryExtents

- RVA: `0x0080F4F8`–`0x0080F526` (길이 `46` bytes)
- VA: `0x000000014080F4F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0080F510` → [MiFreeContiguousPages](../../text/3F/MiFreeContiguousPages_function_003F7178.md) (function, `0x003F7178`)
- `0x0080F51A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiDeletePagefile](../7F/MiDeletePagefile_function_007FFB88.md) at `0x007FFC80`
- [MiCreatePagefileMemoryExtents](MiCreatePagefileMemoryExtents_function_0080F1BC.md) at `0x0080F40E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0080F510` → [MiFreeContiguousPages](../../text/3F/MiFreeContiguousPages_function_003F7178.md) (`PAGE` → `.text`)
  - `0x0080F51A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080F4F8  40 53                           push rbx
0080F4FA  48 83 EC 20                     sub rsp, 0x20
0080F4FE  8B 51 1C                        mov edx, dword ptr [rcx + 0x1c]
0080F501  48 8B D9                        mov rbx, rcx
0080F504  2B 51 18                        sub edx, dword ptr [rcx + 0x18]
0080F507  45 33 C0                        xor r8d, r8d
0080F50A  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
0080F50E  FF C2                           inc edx
0080F510  E8 63 7C BE FF                  call 0x1403f7178
0080F515  33 D2                           xor edx, edx
0080F517  48 8B CB                        mov rcx, rbx
0080F51A  E8 51 33 37 00                  call 0x140b82870
0080F51F  48 83 C4 20                     add rsp, 0x20
0080F523  5B                              pop rbx
0080F524  C3                              ret
0080F525  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeletePageFileMemoryExtents(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 28))) - (*(unsigned int *)(a1 + 24)));
    a3 = 0;
    a2 = (unsigned int)((a2) + 1);
    result = MiFreeContiguousPages(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeletePageFileMemoryExtents(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) - (*(uint32_t *)(arg1 + 0x18)));
    Arg3 = 0;
    Arg2 = (uint32_t)((Arg2) + 1);
    result = MiFreeContiguousPages(*(uint64_t *)(arg1 + 0x20), Arg2, Arg3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080F4F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0080F4F8[BB_0080F4F8]
  bb_0080F525[BB_0080F525]
```
