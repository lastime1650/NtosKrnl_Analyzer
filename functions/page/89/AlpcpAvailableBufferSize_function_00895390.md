# AlpcpAvailableBufferSize

- RVA: `0x00895390`–`0x008953AA` (길이 `26` bytes)
- VA: `0x0000000140895390`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AlpcpCaptureMessageDataSafe](../88/AlpcpCaptureMessageDataSafe_function_0088F3B0.md) at `0x0088F593`
- [AlpcpReceiveLegacyMessage](AlpcpReceiveLegacyMessage_function_00895DE0.md) at `0x00895FA0`
- [AlpcpSendLegacySynchronousRequest](../92/AlpcpSendLegacySynchronousRequest_function_0092376C.md) at `0x00923957`
- [AlpcpSendLegacySynchronousRequest](../92/AlpcpSendLegacySynchronousRequest_function_0092376C.md) at `0x00923C6F`
- [AlpcpReplyLegacySynchronousRequest](../9F/AlpcpReplyLegacySynchronousRequest_function_009F5CF0.md) at `0x009F5FC5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00895390  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00895394  48 85 C0                        test rax, rax
00895397  75 07                           jne 0x1408953a0
00895399  B8 00 02 00 00                  mov eax, 0x200
0089539E  C3                              ret
0089539F  CC                              int3
008953A0  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
008953A4  48 83 E8 28                     sub rax, 0x28
008953A8  C3                              ret
008953A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpAvailableBufferSize(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 96) != 0) goto loc_008953A0;
    return 512;
loc_008953A0:
    result = (*(unsigned __int64 *)(512 + 32)) - (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpAvailableBufferSize(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x60) != 0) goto loc_008953A0;
    return 512;
loc_008953A0:
    result = (*(uint64_t *)(512 + 0x20)) - (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00895390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00895390[BB_00895390]
  bb_00895399[BB_00895399]
  bb_0089539F[BB_0089539F]
  bb_008953A0[BB_008953A0]
  bb_008953A9[BB_008953A9]
  bb_00895390 -->|branch| bb_008953A0
  bb_00895390 -->|fallthrough| bb_00895399
  bb_0089539F -->|flow| bb_008953A0
```
