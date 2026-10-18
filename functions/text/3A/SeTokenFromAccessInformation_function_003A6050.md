# SeTokenFromAccessInformation

- RVA: `0x003A6050`–`0x003A6075` (길이 `37` bytes)
- VA: `0x00000001403A6050`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `12`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A605E` → [SepTokenFromAccessInformation](SepTokenFromAccessInformation_function_003A67A0.md) (function, `0x003A67A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A6050  48 83 EC 28                     sub rsp, 0x28
003A6054  B8 C8 05 00 00                  mov eax, 0x5c8
003A6059  44 3B C0                        cmp r8d, eax
003A605C  72 0D                           jb 0x1403a606b
003A605E  E8 3D 07 00 00                  call 0x1403a67a0
003A6063  33 C0                           xor eax, eax
003A6065  48 83 C4 28                     add rsp, 0x28
003A6069  C3                              ret
003A606A  CC                              int3
003A606B  41 89 01                        mov dword ptr [r9], eax
003A606E  B8 23 00 00 C0                  mov eax, 0xc0000023
003A6073  EB F0                           jmp 0x1403a6065
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeTokenFromAccessInformation(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 < ((unsigned int)((unsigned int)(0x5C8ULL)))) goto loc_003A606B;
    result = SepTokenFromAccessInformation(a1, a2, a3, a4);
    result = 0;
loc_003A6065:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003A606B:
    *(unsigned int *)(a4) = 0;
    goto loc_003A6065;
}
```

## 5. (Beta) C Style

```c
int64_t SeTokenFromAccessInformation(int64_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 < ((uint32_t)((uint32_t)(0x5C8ULL)))) goto loc_003A606B;
    result = SepTokenFromAccessInformation(Arg1, Arg2, Arg3, Arg4);
    result = 0;
loc_003A6065:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003A606B:
    *(uint32_t *)(arg4) = 0;
    goto loc_003A6065;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A6050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A6050[BB_003A6050]
  bb_003A605E[BB_003A605E]
  bb_003A6065[BB_003A6065]
  bb_003A606A[BB_003A606A]
  bb_003A606B[BB_003A606B]
  bb_003A6050 -->|branch| bb_003A606B
  bb_003A6050 -->|fallthrough| bb_003A605E
  bb_003A605E -->|flow| bb_003A6065
  bb_003A606A -->|flow| bb_003A606B
  bb_003A606B -->|branch| bb_003A6065
```
