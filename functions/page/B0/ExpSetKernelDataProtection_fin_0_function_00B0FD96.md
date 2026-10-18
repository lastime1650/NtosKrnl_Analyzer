# ExpSetKernelDataProtection$fin$0

- RVA: `0x00B0FD96`–`0x00B0FDD9` (길이 `67` bytes)
- VA: `0x0000000140B0FD96`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00095048`
- 디코드: `21`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0FDBE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00B0FDCB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B0FDBE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00B0FDCB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0FD96  40 53                           push rbx
00B0FD98  55                              push rbp
00B0FD99  48 83 EC 28                     sub rsp, 0x28
00B0FD9D  48 8B EA                        mov rbp, rdx
00B0FDA0  48 8B 5D 70                     mov rbx, qword ptr [rbp + 0x70]
00B0FDA4  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B0FDA8  F0 48 0F C1 83 B0 B7 00 00      lock xadd qword ptr [rbx + 0xb7b0], rax
00B0FDB1  24 06                           and al, 6
00B0FDB3  3C 02                           cmp al, 2
00B0FDB5  75 0D                           jne 0x140b0fdc4
00B0FDB7  48 8D 8B B0 B7 00 00            lea rcx, [rbx + 0xb7b0]
00B0FDBE  E8 0D 60 75 FF                  call 0x140265dd0
00B0FDC3  90                              nop
00B0FDC4  48 8D 8B B0 B7 00 00            lea rcx, [rbx + 0xb7b0]
00B0FDCB  E8 30 18 7D FF                  call 0x1402e1600
00B0FDD0  90                              nop
00B0FDD1  48 83 C4 28                     add rsp, 0x28
00B0FDD5  5D                              pop rbp
00B0FDD6  5B                              pop rbx
00B0FDD7  C3                              ret
00B0FDD8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSetKernelDataProtection_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = *(unsigned __int64 *)(a2 + 112) + 47024;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a2 + 112) + 47024, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSetKernelDataProtection_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = *(uint64_t *)(arg2 + 0x70) + 47024;
        result = ExfTryToWakePushLock(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg2 + 0x70) + 47024, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0FD96&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0FD96[BB_00B0FD96]
  bb_00B0FDB7[BB_00B0FDB7]
  bb_00B0FDC4[BB_00B0FDC4]
  bb_00B0FDD8[BB_00B0FDD8]
  bb_00B0FD96 -->|branch| bb_00B0FDC4
  bb_00B0FD96 -->|fallthrough| bb_00B0FDB7
  bb_00B0FDB7 -->|flow| bb_00B0FDC4
```
