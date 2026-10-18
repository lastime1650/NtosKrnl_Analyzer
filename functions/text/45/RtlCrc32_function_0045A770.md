# RtlCrc32

- RVA: `0x0045A770`–`0x0045A7C1` (길이 `81` bytes)
- VA: `0x000000014045A770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078D6C`
- 디코드: `24`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0045A788` → [Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline](Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline_function_0045A7C8.md) (function, `0x0045A7C8`)
- `0x0045A79A` → [RtlpCrc32c](RtlpCrc32c_function_0045ACA0.md) (function, `0x0045ACA0`)
- `0x0045A7BA` → [RtlpComputeCrcInternal](RtlpComputeCrcInternal_function_0045A800.md) (function, `0x0045A800`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0045A7B3` → RVA `0x00002ED0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045A770  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0045A775  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0045A77A  57                              push rdi
0045A77B  48 83 EC 20                     sub rsp, 0x20
0045A77F  41 8B F8                        mov edi, r8d
0045A782  48 8B F2                        mov rsi, rdx
0045A785  48 8B D9                        mov rbx, rcx
0045A788  E8 3B 00 00 00                  call 0x14045a7c8
0045A78D  48 8B D6                        mov rdx, rsi
0045A790  48 8B CB                        mov rcx, rbx
0045A793  85 C0                           test eax, eax
0045A795  74 19                           je 0x14045a7b0
0045A797  44 8B C7                        mov r8d, edi
0045A79A  E8 01 05 00 00                  call 0x14045aca0
0045A79F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0045A7A4  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0045A7A9  48 83 C4 20                     add rsp, 0x20
0045A7AD  5F                              pop rdi
0045A7AE  C3                              ret
0045A7AF  CC                              int3
0045A7B0  4C 8B C7                        mov r8, rdi
0045A7B3  4C 8D 0D 16 87 BA FF            lea r9, [rip - 0x4578ea]
0045A7BA  E8 41 00 00 00                  call 0x14045a800
0045A7BF  EB DE                           jmp 0x14045a79f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCrc32(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0045A7B0;
    result = RtlpCrc32c(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
loc_0045A79F:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0045A7B0:
    result = RtlpComputeCrcInternal(a1, a2, (unsigned int)(a3), v_rip - 4552938);
    goto loc_0045A79F;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCrc32(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_0045A7B0;
    result = RtlpCrc32c(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
loc_0045A79F:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0045A7B0:
    result = RtlpComputeCrcInternal(Arg1, Arg2, (uint32_t)(Arg3), v_rip - 4552938);
    goto loc_0045A79F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045A770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045A770[BB_0045A770]
  bb_0045A797[BB_0045A797]
  bb_0045A79F[BB_0045A79F]
  bb_0045A7AF[BB_0045A7AF]
  bb_0045A7B0[BB_0045A7B0]
  bb_0045A770 -->|branch| bb_0045A7B0
  bb_0045A770 -->|fallthrough| bb_0045A797
  bb_0045A797 -->|flow| bb_0045A79F
  bb_0045A7AF -->|flow| bb_0045A7B0
  bb_0045A7B0 -->|branch| bb_0045A79F
```
