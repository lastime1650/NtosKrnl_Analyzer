# PnpFreeDevProperty

- RVA: `0x008DB29C`–`0x008DB2D5` (길이 `57` bytes)
- VA: `0x00000001408DB29C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DB2B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008DB2C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PnpCopyDevProperty](PnpCopyDevProperty_function_008DB1CC.md) at `0x008DB277`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008DB2B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008DB2C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DB29C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DB2A1  57                              push rdi
008DB2A2  48 83 EC 20                     sub rsp, 0x20
008DB2A6  48 8B F9                        mov rdi, rcx
008DB2A9  8B DA                           mov ebx, edx
008DB2AB  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
008DB2AF  48 85 C9                        test rcx, rcx
008DB2B2  74 05                           je 0x1408db2b9
008DB2B4  E8 B7 75 2A 00                  call 0x140b82870
008DB2B9  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
008DB2BD  48 85 C9                        test rcx, rcx
008DB2C0  74 07                           je 0x1408db2c9
008DB2C2  8B D3                           mov edx, ebx
008DB2C4  E8 A7 75 2A 00                  call 0x140b82870
008DB2C9  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008DB2CE  48 83 C4 20                     add rsp, 0x20
008DB2D2  5F                              pop rdi
008DB2D3  C3                              ret
008DB2D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpFreeDevProperty(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 40) != 0) {
        a2 = (unsigned int)((unsigned int)(a2));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpFreeDevProperty(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x18), Arg2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x28) != 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x28), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DB29C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008DB29C[BB_008DB29C]
  bb_008DB2B4[BB_008DB2B4]
  bb_008DB2B9[BB_008DB2B9]
  bb_008DB2C2[BB_008DB2C2]
  bb_008DB2C9[BB_008DB2C9]
  bb_008DB2D4[BB_008DB2D4]
  bb_008DB29C -->|branch| bb_008DB2B9
  bb_008DB29C -->|fallthrough| bb_008DB2B4
  bb_008DB2B4 -->|flow| bb_008DB2B9
  bb_008DB2B9 -->|branch| bb_008DB2C9
  bb_008DB2B9 -->|fallthrough| bb_008DB2C2
  bb_008DB2C2 -->|flow| bb_008DB2C9
```
