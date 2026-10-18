# AlpcpUnlockBlobUncachedExclusive

- RVA: `0x0092536C`–`0x0092539C` (길이 `48` bytes)
- VA: `0x000000014092536C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00925388` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00925390` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [NtAlpcRevokeSecurityContext](../74/NtAlpcRevokeSecurityContext_function_0074C400.md) at `0x0074C4C7`
- [AlpcConnectionDestroyProcedure](AlpcConnectionDestroyProcedure_function_00924310.md) at `0x009243B1`
- [AlpcpDisconnectPort](AlpcpDisconnectPort_function_00924A68.md) at `0x00924B80`
- [AlpcpDisconnectPort](AlpcpDisconnectPort_function_00924A68.md) at `0x00924D77`
- [AlpcpDeletePort](AlpcpDeletePort_function_00925010.md) at `0x0092508E`
- [AlpcpWalkConnectionList](AlpcpWalkConnectionList_function_00925D20.md) at `0x00925D49`
- [AlpcpCreateClientPort](AlpcpCreateClientPort_function_009270AC.md) at `0x00927381`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34A13`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00925388` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00925390` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092536C  40 53                           push rbx
0092536E  48 83 EC 20                     sub rsp, 0x20
00925372  48 8D 59 F0                     lea rbx, [rcx - 0x10]
00925376  48 83 C8 FF                     or rax, 0xffffffffffffffff
0092537A  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0092537F  24 06                           and al, 6
00925381  3C 02                           cmp al, 2
00925383  75 08                           jne 0x14092538d
00925385  48 8B CB                        mov rcx, rbx
00925388  E8 43 0A 94 FF                  call 0x140265dd0
0092538D  48 8B CB                        mov rcx, rbx
00925390  E8 6B C2 9B FF                  call 0x1402e1600
00925395  48 83 C4 20                     add rsp, 0x20
00925399  5B                              pop rbx
0092539A  C3                              ret
0092539B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpUnlockBlobUncachedExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 - 16;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 - 16, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpUnlockBlobUncachedExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 - 16;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 - 16, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x10` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092536C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0092536C[BB_0092536C]
  bb_00925385[BB_00925385]
  bb_0092538D[BB_0092538D]
  bb_0092539B[BB_0092539B]
  bb_0092536C -->|branch| bb_0092538D
  bb_0092536C -->|fallthrough| bb_00925385
  bb_00925385 -->|flow| bb_0092538D
```
