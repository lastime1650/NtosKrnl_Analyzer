# PipFreeBindingRequestEntry

- RVA: `0x00727C84`–`0x00727CC8` (길이 `68` bytes)
- VA: `0x0000000140727C84`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00727C9C` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00727CAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00727CBC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PipFreeDependencyEdge](../../text/4D/PipFreeDependencyEdge_function_004D7658.md) at `0x004D7697`
- [PipAddRequestToEdge](PipAddRequestToEdge_function_00727898.md) at `0x0072797F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00727CAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00727CBC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00727C84  40 53                           push rbx
00727C86  48 83 EC 20                     sub rsp, 0x20
00727C8A  83 79 10 01                     cmp dword ptr [rcx + 0x10], 1
00727C8E  48 8B D9                        mov rbx, rcx
00727C91  75 21                           jne 0x140727cb4
00727C93  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00727C97  48 85 C9                        test rcx, rcx
00727C9A  74 18                           je 0x140727cb4
00727C9C  E8 5F 8B 29 00                  call 0x1409c0800
00727CA1  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00727CA5  BA 50 6E 70 53                  mov edx, 0x53706e50
00727CAA  E8 C1 AB 45 00                  call 0x140b82870
00727CAF  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
00727CB4  BA 50 6E 70 53                  mov edx, 0x53706e50
00727CB9  48 8B CB                        mov rcx, rbx
00727CBC  E8 AF AB 45 00                  call 0x140b82870
00727CC1  48 83 C4 20                     add rsp, 0x20
00727CC5  5B                              pop rbx
00727CC6  C3                              ret
00727CC7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipFreeBindingRequestEntry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(a1 + 16)) != 1) goto loc_00727CB4;
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        result = RtlFreeAnsiString(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
        a1 = *(unsigned __int64 *)(a1 + 24);
        a2 = 0x53706E50ULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExFreePoolWithTag(a1, (unsigned int)(0x53706E50ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipFreeBindingRequestEntry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(arg1 + 0x10)) != 1) goto loc_00727CB4;
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        result = RtlFreeAnsiString(*(uint64_t *)(arg1 + 0x18), a2, a3, a4);
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        a2 = 0x53706E50ULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x53706E50ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00727C84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00727C84[BB_00727C84]
  bb_00727C93[BB_00727C93]
  bb_00727C9C[BB_00727C9C]
  bb_00727CB4[BB_00727CB4]
  bb_00727CC7[BB_00727CC7]
  bb_00727C84 -->|branch| bb_00727CB4
  bb_00727C84 -->|fallthrough| bb_00727C93
  bb_00727C93 -->|branch| bb_00727CB4
  bb_00727C93 -->|fallthrough| bb_00727C9C
  bb_00727C9C -->|flow| bb_00727CB4
```
