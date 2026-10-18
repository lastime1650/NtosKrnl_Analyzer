# DECREMENT_SCATTER_GATHER_LISTS

- RVA: `0x00B94C44`–`0x00B94CD0` (길이 `140` bytes)
- VA: `0x0000000140B94C44`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000733E4`
- 디코드: `34`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B94C93` → [ViHalPreprocessOptions](ViHalPreprocessOptions_function_00B9920C.md) (function, `0x00B9920C`)
- `0x00B94CBA` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (function, `0x00614444`)

### Direct callers
- [VfBuildScatterGatherList](VfBuildScatterGatherList_function_00B95AA0.md) at `0x00B95D01`
- [VfBuildScatterGatherListEx](VfBuildScatterGatherListEx_function_00B95DA0.md) at `0x00B95F2B`
- [VfGetScatterGatherList](VfGetScatterGatherList_function_00B96BD0.md) at `0x00B96D5B`
- [VfGetScatterGatherList](VfGetScatterGatherList_function_00B96BD0.md) at `0x00B96E8A`
- [VfGetScatterGatherListEx](VfGetScatterGatherListEx_function_00B96F20.md) at `0x00B9707B`
- [VfPutScatterGatherList](VfPutScatterGatherList_function_00B97970.md) at `0x00B97A50`
- [VfPutScatterGatherList](VfPutScatterGatherList_function_00B97970.md) at `0x00B97ABC`

### Static image references
- `0x00B94C6E` → RVA `0x00E0E9C0` (`.data`; read)
- `0x00B94C8C` → RVA `0x00BBA5F0` (` ?? ::JKADOLAD::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B94CBA` → [VfReportIssueWithOptions](../../text/61/VfReportIssueWithOptions_function_00614444.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B94C44  48 8B C4                        mov rax, rsp
00B94C47  48 89 58 08                     mov qword ptr [rax + 8], rbx
00B94C4B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00B94C4F  57                              push rdi
00B94C50  48 83 EC 30                     sub rsp, 0x30
00B94C54  48 8B F9                        mov rdi, rcx
00B94C57  83 CB FF                        or ebx, 0xffffffff
00B94C5A  F0 0F C1 99 C8 00 00 00         lock xadd dword ptr [rcx + 0xc8], ebx
00B94C62  83 EB 01                        sub ebx, 1
00B94C65  79 58                           jns 0x140b94cbf
00B94C67  44 8B 89 C4 00 00 00            mov r9d, dword ptr [rcx + 0xc4]
00B94C6E  48 8D 35 4B 9D 27 00            lea rsi, [rip + 0x279d4b]
00B94C75  48 83 60 F0 00                  and qword ptr [rax - 0x10], 0
00B94C7A  41 8B D1                        mov edx, r9d
00B94C7D  2B D3                           sub edx, ebx
00B94C7F  41 B8 06 00 00 00               mov r8d, 6
00B94C85  48 89 50 E8                     mov qword ptr [rax - 0x18], rdx
00B94C89  48 8B CE                        mov rcx, rsi
00B94C8C  48 8D 15 5D 59 02 00            lea rdx, [rip + 0x2595d]
00B94C93  E8 74 45 00 00                  call 0x140b9920c
00B94C98  44 8B 87 C4 00 00 00            mov r8d, dword ptr [rdi + 0xc4]
00B94C9F  BA 06 00 00 00                  mov edx, 6
00B94CA4  45 8B C8                        mov r9d, r8d
00B94CA7  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00B94CAC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B94CB2  44 2B CB                        sub r9d, ebx
00B94CB5  B9 E6 00 00 00                  mov ecx, 0xe6
00B94CBA  E8 85 F7 A7 FF                  call 0x140614444
00B94CBF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00B94CC4  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00B94CC9  48 83 C4 30                     add rsp, 0x30
00B94CCD  5F                              pop rdi
00B94CCE  C3                              ret
00B94CCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DECREMENT_SCATTER_GATHER_LISTS(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
    v_rbx = (unsigned int)((v_rbx) - (1));
    result = v_rsp;
    if (sign_flag) {
        a4 = *(unsigned int *)(a1 + 196);
        v_rsi = v_rip + 2596171;
        a2 = (unsigned int)(a4);
        a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx)));
        a3 = 6;
        *(unsigned __int64 *)(v_rsp - 24) = a2;
        a1 = v_rsi;
        a2 = v_rip + 153949;
        result = ViHalPreprocessOptions(a1, a2, a3, a4);
        a3 = *(unsigned int *)(a1 + 196);
        a2 = 6;
        a4 = (unsigned int)(a3);
        v_stack_m10 = v_rsi;
        a4 = (unsigned int)((a4) - ((unsigned int)(v_rbx)));
        a1 = 230;
        result = VfReportIssueWithOptions(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DECREMENT_SCATTER_GATHER_LISTS(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
    local_rbx = (uint32_t)((local_rbx) - (1));
    result = local_rsp;
    if (sign_flag) {
        a4 = *(uint32_t *)(arg1 + 0xC4);
        local_rsi = v_rip + 2596171;
        a2 = (uint32_t)(a4);
        a2 = (uint32_t)((a2) - ((uint32_t)(local_rbx)));
        a3 = 6;
        *(uint64_t *)(local_rsp - 0x18) = a2;
        Arg1 = local_rsi;
        a2 = v_rip + 153949;
        result = ViHalPreprocessOptions(Arg1, a2, a3, a4);
        a3 = *(uint32_t *)(arg1 + 0xC4);
        a2 = 6;
        a4 = (uint32_t)(a3);
        v_stack_m10 = local_rsi;
        a4 = (uint32_t)((a4) - ((uint32_t)(local_rbx)));
        Arg1 = 230;
        result = VfReportIssueWithOptions(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC4` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B94C44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B94C44[BB_00B94C44]
  bb_00B94C67[BB_00B94C67]
  bb_00B94CBF[BB_00B94CBF]
  bb_00B94CCF[BB_00B94CCF]
  bb_00B94C44 -->|branch| bb_00B94CBF
  bb_00B94C44 -->|fallthrough| bb_00B94C67
  bb_00B94C67 -->|flow| bb_00B94CBF
```
