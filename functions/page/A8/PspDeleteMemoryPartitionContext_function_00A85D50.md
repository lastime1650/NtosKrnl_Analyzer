# PspDeleteMemoryPartitionContext

- RVA: `0x00A85D50`–`0x00A85D6B` (길이 `27` bytes)
- VA: `0x0000000140A85D50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090138`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A85D64` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [PsCreateMinimalProcess](../78/PsCreateMinimalProcess_function_00786D14.md) at `0x007870C3`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB809`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A85D64` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A85D50  48 83 EC 28                     sub rsp, 0x28
00A85D54  48 85 C9                        test rcx, rcx
00A85D57  75 06                           jne 0x140a85d5f
00A85D59  48 83 C4 28                     add rsp, 0x28
00A85D5D  C3                              ret
00A85D5E  CC                              int3
00A85D5F  BA 50 73 4A 62                  mov edx, 0x624a7350
00A85D64  E8 77 1B 87 FF                  call 0x1402f78e0
00A85D69  EB EE                           jmp 0x140a85d59
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspDeleteMemoryPartitionContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_00A85D5F;
loc_00A85D59:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A85D5F:
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x624A7350ULL), a3, a4);
    goto loc_00A85D59;
}
```

## 5. (Beta) C Style

```c
int64_t PspDeleteMemoryPartitionContext(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_00A85D5F;
loc_00A85D59:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A85D5F:
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x624A7350ULL), a3, a4);
    goto loc_00A85D59;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A85D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A85D50[BB_00A85D50]
  bb_00A85D59[BB_00A85D59]
  bb_00A85D5E[BB_00A85D5E]
  bb_00A85D5F[BB_00A85D5F]
  bb_00A85D50 -->|branch| bb_00A85D5F
  bb_00A85D50 -->|fallthrough| bb_00A85D59
  bb_00A85D5E -->|flow| bb_00A85D5F
  bb_00A85D5F -->|branch| bb_00A85D59
```
