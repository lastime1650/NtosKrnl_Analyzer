# AlpcpEndInitialization

- RVA: `0x00A20C78`–`0x00A20CB1` (길이 `57` bytes)
- VA: `0x0000000140A20C78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A20C9D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A20CA5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [AlpcpCreateSecurityContext](../89/AlpcpCreateSecurityContext_function_00890D94.md) at `0x00891024`
- [AlpcpCreateReserve](../89/AlpcpCreateReserve_function_00892318.md) at `0x00892530`
- [AlpcpCreateSection](../89/AlpcpCreateSection_function_0089307C.md) at `0x0089325D`
- [sub_00B19414](../B1/Unknown_function_00B19414.md) at `0x00B19422`
- [sub_00B194AC](../B1/Unknown_function_00B194AC.md) at `0x00B194BB`
- [sub_00B195F6](../B1/Unknown_function_00B195F6.md) at `0x00B19605`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A20C9D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A20CA5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A20C78  40 53                           push rbx
00A20C7A  48 83 EC 20                     sub rsp, 0x20
00A20C7E  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00A20C83  80 61 E0 FB                     and byte ptr [rcx - 0x20], 0xfb
00A20C87  48 8D 59 F0                     lea rbx, [rcx - 0x10]
00A20C8B  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A20C8F  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
00A20C94  24 06                           and al, 6
00A20C96  3C 02                           cmp al, 2
00A20C98  75 08                           jne 0x140a20ca2
00A20C9A  48 8B CB                        mov rcx, rbx
00A20C9D  E8 2E 51 84 FF                  call 0x140265dd0
00A20CA2  48 8B CB                        mov rcx, rbx
00A20CA5  E8 56 09 8C FF                  call 0x1402e1600
00A20CAA  48 83 C4 20                     add rsp, 0x20
00A20CAE  5B                              pop rbx
00A20CAF  C3                              ret
00A20CB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpEndInitialization(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;

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
int64_t AlpcpEndInitialization(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;

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
| `Arg1` | `- 0x20` | `8` | `R/W` |
| `Arg1` | `- 0x10` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A20C78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A20C78[BB_00A20C78]
  bb_00A20C9A[BB_00A20C9A]
  bb_00A20CA2[BB_00A20CA2]
  bb_00A20CB0[BB_00A20CB0]
  bb_00A20C78 -->|branch| bb_00A20CA2
  bb_00A20C78 -->|fallthrough| bb_00A20C9A
  bb_00A20C9A -->|flow| bb_00A20CA2
```
