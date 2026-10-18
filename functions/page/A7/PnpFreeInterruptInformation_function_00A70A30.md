# PnpFreeInterruptInformation

- RVA: `0x00A70A30`–`0x00A70A68` (길이 `56` bytes)
- VA: `0x0000000140A70A30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C174`
- 디코드: `16`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A70A55` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) at `0x0026FF18`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A70A55` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A70A30  40 53                           push rbx
00A70A32  48 83 EC 20                     sub rsp, 0x20
00A70A36  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00A70A3D  48 8B D9                        mov rbx, rcx
00A70A40  48 8B 48 58                     mov rcx, qword ptr [rax + 0x58]
00A70A44  48 85 C9                        test rcx, rcx
00A70A47  75 07                           jne 0x140a70a50
00A70A49  48 83 C4 20                     add rsp, 0x20
00A70A4D  5B                              pop rbx
00A70A4E  C3                              ret
00A70A4F  CC                              int3
00A70A50  BA 50 6E 70 47                  mov edx, 0x47706e50
00A70A55  E8 16 1E 11 00                  call 0x140b82870
00A70A5A  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00A70A61  48 83 60 58 00                  and qword ptr [rax + 0x58], 0
00A70A66  EB E1                           jmp 0x140a70a49
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpFreeInterruptInformation(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 88) != 0) goto loc_00A70A50;
loc_00A70A49:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 312);
loc_00A70A50:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 88), (unsigned int)(0x47706E50ULL), a3, a4);
    goto loc_00A70A49;
}
```

## 5. (Beta) C Style

```c
int64_t PnpFreeInterruptInformation(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138) + 0x58) != 0) goto loc_00A70A50;
loc_00A70A49:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x138);
loc_00A70A50:
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x138) + 0x58), (uint32_t)(0x47706E50ULL), a3, a4);
    goto loc_00A70A49;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x138` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A70A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A70A30[BB_00A70A30]
  bb_00A70A49[BB_00A70A49]
  bb_00A70A4F[BB_00A70A4F]
  bb_00A70A50[BB_00A70A50]
  bb_00A70A30 -->|branch| bb_00A70A50
  bb_00A70A30 -->|fallthrough| bb_00A70A49
  bb_00A70A4F -->|flow| bb_00A70A50
  bb_00A70A50 -->|branch| bb_00A70A49
```
