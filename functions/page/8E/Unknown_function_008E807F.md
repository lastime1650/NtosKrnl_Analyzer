# sub_008E807F

- RVA: `0x008E807F`–`0x008E80AE` (길이 `47` bytes)
- VA: `0x00000001408E807F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086960`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008E80A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008E80A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E807F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E8088  80 B8 32 02 00 00 00            cmp byte ptr [rax + 0x232], 0
008E808F  75 0C                           jne 0x1408e809d
008E8091  8B C3                           mov eax, ebx
008E8093  48 81 C4 C0 00 00 00            add rsp, 0xc0
008E809A  5B                              pop rbx
008E809B  C3                              ret
008E809C  CC                              int3
008E809D  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
008E80A5  33 D2                           xor edx, edx
008E80A7  E8 C4 A7 29 00                  call 0x140b82870
008E80AC  EB E3                           jmp 0x1408e8091
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E807F(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;
    __int64 v_rsp;

    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008E809D;
loc_008E8091:
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)(v_rbx));
loc_008E809D:
    a2 = 0;
    result = ExFreePoolWithTag(a17, a2, a3, a4);
    goto loc_008E8091;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008E807F(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, int64_t Arg17)
{
    int64_t result;
    int64_t local_rsp;

    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008E809D;
loc_008E8091:
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)(local_rbx));
loc_008E809D:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg17, Arg2, Arg3, Arg4);
    goto loc_008E8091;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E807F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E807F[BB_008E807F]
  bb_008E8091[BB_008E8091]
  bb_008E809C[BB_008E809C]
  bb_008E809D[BB_008E809D]
  bb_008E807F -->|branch| bb_008E809D
  bb_008E807F -->|fallthrough| bb_008E8091
  bb_008E809C -->|flow| bb_008E809D
  bb_008E809D -->|branch| bb_008E8091
```
