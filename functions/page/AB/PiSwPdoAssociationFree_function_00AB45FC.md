# PiSwPdoAssociationFree

- RVA: `0x00AB45FC`–`0x00AB462B` (길이 `47` bytes)
- VA: `0x0000000140AB45FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB4609` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AB4612` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AB461F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiSwFreePdoAssociationsList](../8D/PiSwFreePdoAssociationsList_function_008DA5B8.md) at `0x008DA619`
- [PiSwRemovePdoAssociation](../94/PiSwRemovePdoAssociation_function_0094E8E0.md) at `0x0094E96D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AB4609` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AB4612` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AB461F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB45FC  40 53                           push rbx
00AB45FE  48 83 EC 20                     sub rsp, 0x20
00AB4602  48 8B D9                        mov rbx, rcx
00AB4605  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00AB4609  E8 42 4D 84 FF                  call 0x1402f9350
00AB460E  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00AB4612  E8 39 4D 84 FF                  call 0x1402f9350
00AB4617  BA 50 6E 70 57                  mov edx, 0x57706e50
00AB461C  48 8B CB                        mov rcx, rbx
00AB461F  E8 4C E2 0C 00                  call 0x140b82870
00AB4624  48 83 C4 20                     add rsp, 0x20
00AB4628  5B                              pop rbx
00AB4629  C3                              ret
00AB462A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwPdoAssociationFree(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ObfDereferenceObject(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    result = ObfDereferenceObject(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    result = ExFreePoolWithTag(a1, (unsigned int)(0x57706E50ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwPdoAssociationFree(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ObfDereferenceObject(*(uint64_t *)(arg1 + 0x20), a2, a3, a4);
    result = ObfDereferenceObject(*(uint64_t *)(arg1 + 0x28), a2, a3, a4);
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x57706E50ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB45FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB45FC[BB_00AB45FC]
  bb_00AB462A[BB_00AB462A]
```
