# PfpPartitionCleanup

- RVA: `0x00752050`–`0x00752078` (길이 `40` bytes)
- VA: `0x0000000140752050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0075205E` → [PfTCleanup](PfTCleanup_function_00751208.md) (function, `0x00751208`)
- `0x0075206C` → [ExFreeCacheAwareRundownProtection](../../text/48/ExFreeCacheAwareRundownProtection_function_0048FDD0.md) (function, `0x0048FDD0`)

### Direct callers
- [PfpPartitionCreate](../../text/5C/PfpPartitionCreate_function_005CDE8C.md) at `0x005CDF84`
- [PfDeletePartition](PfDeletePartition_function_00751EB4.md) at `0x00751F62`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0075206C` → [ExFreeCacheAwareRundownProtection](../../text/48/ExFreeCacheAwareRundownProtection_function_0048FDD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00752050  40 53                           push rbx
00752052  48 83 EC 20                     sub rsp, 0x20
00752056  BA 01 00 00 00                  mov edx, 1
0075205B  48 8B D9                        mov rbx, rcx
0075205E  E8 A5 F1 FF FF                  call 0x140751208
00752063  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00752067  48 85 C9                        test rcx, rcx
0075206A  74 05                           je 0x140752071
0075206C  E8 5F DD D3 FF                  call 0x14048fdd0
00752071  48 83 C4 20                     add rsp, 0x20
00752075  5B                              pop rbx
00752076  C3                              ret
00752077  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpPartitionCleanup(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PfTCleanup(a1, 1, a3, a4);
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        result = ExFreeCacheAwareRundownProtection(*(unsigned __int64 *)(a1 + 16), 1, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpPartitionCleanup(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PfTCleanup(Arg1, 1, a3, a4);
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        result = ExFreeCacheAwareRundownProtection(*(uint64_t *)(arg1 + 0x10), 1, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00752050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00752050[BB_00752050]
  bb_0075206C[BB_0075206C]
  bb_00752071[BB_00752071]
  bb_00752077[BB_00752077]
  bb_00752050 -->|branch| bb_00752071
  bb_00752050 -->|fallthrough| bb_0075206C
  bb_0075206C -->|flow| bb_00752071
```
