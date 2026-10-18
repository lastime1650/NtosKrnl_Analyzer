# sub_00C19340

- RVA: `0x00C19340`–`0x00C1938D` (길이 `77` bytes)
- VA: `0x0000000140C19340`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `22`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C1935F` → [PsQueryThreadStartAddress](../../text/3F/PsQueryThreadStartAddress_function_003FCF00.md) (function, `0x003FCF00`)
- `0x00C19373` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C19364` → RVA `0x005D93E0` (`PopIrpWorkerControl`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C1935F` → [PsQueryThreadStartAddress](../../text/3F/PsQueryThreadStartAddress_function_003FCF00.md) (`INIT` → `.text`)
  - `0x00C19373` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C19340  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C19345  57                              push rdi
00C19346  48 83 EC 20                     sub rsp, 0x20
00C1934A  49 83 B8 E0 09 00 00 00         cmp qword ptr [r8 + 0x9e0], 0
00C19352  49 8B F8                        mov rdi, r8
00C19355  48 8B DA                        mov rbx, rdx
00C19358  75 25                           jne 0x140c1937f
00C1935A  33 D2                           xor edx, edx
00C1935C  48 8B CB                        mov rcx, rbx
00C1935F  E8 9C 3B 7E FF                  call 0x1403fcf00
00C19364  48 8D 0D 75 00 9C FF            lea rcx, [rip - 0x63ff8b]
00C1936B  48 3B C1                        cmp rax, rcx
00C1936E  75 0F                           jne 0x140c1937f
00C19370  48 8B CB                        mov rcx, rbx
00C19373  E8 A8 66 5F FF                  call 0x14020fa20
00C19378  48 89 9F E0 09 00 00            mov qword ptr [rdi + 0x9e0], rbx
00C1937F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00C19384  33 C0                           xor eax, eax
00C19386  48 83 C4 20                     add rsp, 0x20
00C1938A  5F                              pop rdi
00C1938B  C3                              ret
00C1938C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C19340(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(a3 + 2528)) != 0) goto loc_00C1937F;
    a2 = 0;
    result = PsQueryThreadStartAddress(0, a2, a3, a4);
    if (result == (v_rip - 6553483)) {
        a1 = 0;
        result = ObfReferenceObject(a1, a2, a3, a4);
        *(unsigned __int64 *)(a3 + 2528) = 0;
    }
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C19340(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(arg3 + 0x9E0)) != 0) goto loc_00C1937F;
    Arg2 = 0;
    result = PsQueryThreadStartAddress(0, Arg2, Arg3, a4);
    if (result == (v_rip - 6553483)) {
        Arg1 = 0;
        result = ObfReferenceObject(Arg1, Arg2, Arg3, a4);
        *(uint64_t *)(arg3 + 0x9E0) = 0;
    }
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x9E0` | `64` | `R` |
| `Arg3` | `+ 0x9E0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C19340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C19340[BB_00C19340]
  bb_00C1935A[BB_00C1935A]
  bb_00C19370[BB_00C19370]
  bb_00C1937F[BB_00C1937F]
  bb_00C1938C[BB_00C1938C]
  bb_00C19340 -->|branch| bb_00C1937F
  bb_00C19340 -->|fallthrough| bb_00C1935A
  bb_00C1935A -->|branch| bb_00C1937F
  bb_00C1935A -->|fallthrough| bb_00C19370
  bb_00C19370 -->|flow| bb_00C1937F
```
