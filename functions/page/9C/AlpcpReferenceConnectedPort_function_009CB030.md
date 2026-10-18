# AlpcpReferenceConnectedPort

- RVA: `0x009CB030`–`0x009CB052` (길이 `34` bytes)
- VA: `0x00000001409CB030`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0C10`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtAlpcImpersonateClientOfPort](../89/NtAlpcImpersonateClientOfPort_function_008961A0.md) at `0x008966CA`
- [sub_00896999](../89/Unknown_function_00896999.md) at `0x008969D1`
- [AlpcpPortQueryServerSessionInfo](AlpcpPortQueryServerSessionInfo_function_009CAB0C.md) at `0x009CAB38`
- [AlpcpPortQueryConnectedSidInfo](AlpcpPortQueryConnectedSidInfo_function_009CAC3C.md) at `0x009CACB9`
- [AlpcpExposeHandleAttribute](AlpcpExposeHandleAttribute_function_009CAE60.md) at `0x009CAF98`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009CB04C` → [sub_009CB10D](Unknown_function_009CB10D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009CB030  40 53                           push rbx
009CB032  57                              push rdi
009CB033  41 57                           push r15
009CB035  48 83 EC 30                     sub rsp, 0x30
009CB039  8B 81 A0 01 00 00               mov eax, dword ptr [rcx + 0x1a0]
009CB03F  45 33 FF                        xor r15d, r15d
009CB042  24 06                           and al, 6
009CB044  48 8B D9                        mov rbx, rcx
009CB047  41 8B FF                        mov edi, r15d
009CB04A  3C 02                           cmp al, 2
009CB04C  0F 84 BB 00 00 00               je 0x1409cb10d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReferenceConnectedPort(__int64 a1)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    v_r15 = 0;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 416))) & (6));
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReferenceConnectedPort(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    local_r15 = 0;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1A0))) & (6));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009CB030&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009CB030[BB_009CB030]
```
