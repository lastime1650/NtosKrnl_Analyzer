# EtwTimLogProhibitDynamicCode

- RVA: `0x00A8E9DC`–`0x00A8EA2B` (길이 `79` bytes)
- VA: `0x0000000140A8E9DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B71CC`
- 디코드: `20`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A8EA19` → [EtwpTimLogMitigationForProcess](EtwpTimLogMitigationForProcess_function_00A81E6C.md) (function, `0x00A81E6C`)

### Direct callers
- [MiArbitraryCodeBlocked](../97/MiArbitraryCodeBlocked_function_0097D7CC.md) at `0x0097D839`

### Static image references
- `0x00A8EA00` → RVA `0x00021310` (`.rdata`; read)
- `0x00A8EA09` → RVA `0x000234A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8E9DC  40 53                           push rbx
00A8E9DE  48 83 EC 30                     sub rsp, 0x30
00A8E9E2  F7 82 50 07 00 00 00 08 00 00   test dword ptr [rdx + 0x750], 0x800
00A8E9EC  48 8B DA                        mov rbx, rdx
00A8E9EF  75 07                           jne 0x140a8e9f8
00A8E9F1  48 83 C4 30                     add rsp, 0x30
00A8E9F5  5B                              pop rbx
00A8E9F6  C3                              ret
00A8E9F7  CC                              int3
00A8E9F8  83 F9 01                        cmp ecx, 1
00A8E9FB  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00A8EA00  48 8D 05 09 29 59 FF            lea rax, [rip - 0xa6d6f7]
00A8EA07  8B D1                           mov edx, ecx
00A8EA09  4C 8D 05 90 4A 59 FF            lea r8, [rip - 0xa6b570]
00A8EA10  4C 8B CB                        mov r9, rbx
00A8EA13  4C 0F 45 C0                     cmovne r8, rax
00A8EA17  33 C9                           xor ecx, ecx
00A8EA19  E8 4E 34 FF FF                  call 0x140a81e6c
00A8EA1E  F0 81 A3 50 07 00 00 FF F7 FF FF  lock and dword ptr [rbx + 0x750], 0xfffff7ff
00A8EA29  EB C6                           jmp 0x140a8e9f1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTimLogProhibitDynamicCode(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p20;

    v_rsp = (v_rsp) - (48);
    if (((*(unsigned int *)(a2 + 1872)) & (0x800ULL)) != 0) goto loc_00A8E9F8;
loc_00A8E9F1:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00A8E9F8:
    v_stack_p20 = 1;
    a3 = v_rip - 10925424;
    if (a1 != 1) { a3 = v_rip - 10934007; }
    a1 = 0;
    result = EtwpTimLogMitigationForProcess(a1, (unsigned int)(a1), a3, a2);
    goto loc_00A8E9F1;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTimLogProhibitDynamicCode(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p20;

    local_rsp = (local_rsp) - (48);
    if (((*(uint32_t *)(arg2 + 0x750)) & (0x800ULL)) != 0) goto loc_00A8E9F8;
loc_00A8E9F1:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00A8E9F8:
    v_stack_p20 = 1;
    a3 = v_rip - 10925424;
    if (Arg1 != 1) { a3 = v_rip - 10934007; }
    Arg1 = 0;
    result = EtwpTimLogMitigationForProcess(Arg1, (uint32_t)(Arg1), a3, Arg2);
    goto loc_00A8E9F1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x750` | `32` | `R` |
| `Arg2` | `+ 0x750` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8E9DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8E9DC[BB_00A8E9DC]
  bb_00A8E9F1[BB_00A8E9F1]
  bb_00A8E9F7[BB_00A8E9F7]
  bb_00A8E9F8[BB_00A8E9F8]
  bb_00A8E9DC -->|branch| bb_00A8E9F8
  bb_00A8E9DC -->|fallthrough| bb_00A8E9F1
  bb_00A8E9F7 -->|flow| bb_00A8E9F8
  bb_00A8E9F8 -->|branch| bb_00A8E9F1
```
