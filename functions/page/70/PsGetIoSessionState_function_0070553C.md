# PsGetIoSessionState

- RVA: `0x0070553C`–`0x00705552` (길이 `22` bytes)
- VA: `0x000000014070553C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoGetContainerInformation](../71/IoGetContainerInformation_function_0071E680.md) at `0x0071E6CE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070553C  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00705540  48 85 D2                        test rdx, rdx
00705543  74 05                           je 0x14070554a
00705545  8B 48 08                        mov ecx, dword ptr [rax + 8]
00705548  89 0A                           mov dword ptr [rdx], ecx
0070554A  8B 80 80 00 00 00               mov eax, dword ptr [rax + 0x80]
00705550  C3                              ret
00705551  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetIoSessionState(__int64 a1, __int64 a2)
{
    if (a2 != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 8);
        *(unsigned int *)(a2) = (unsigned int)(a1);
    }
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 128));
}
```

## 5. (Beta) C Style

```c
int64_t PsGetIoSessionState(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8);
        *(uint32_t *)(Arg2) = (uint32_t)(Arg1);
    }
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x80));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070553C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070553C[BB_0070553C]
  bb_00705545[BB_00705545]
  bb_0070554A[BB_0070554A]
  bb_00705551[BB_00705551]
  bb_0070553C -->|branch| bb_0070554A
  bb_0070553C -->|fallthrough| bb_00705545
  bb_00705545 -->|flow| bb_0070554A
```
