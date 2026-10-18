# KiVerifyXcptFinally$fin$0

- RVA: `0x00C8040D`–`0x00C80446` (길이 `57` bytes)
- VA: `0x0000000140C8040D`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `18`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C80439` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C8042E` → RVA `0x00C3AE15` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C80439` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C8040D  40 55                           push rbp
00C8040F  48 83 EC 20                     sub rsp, 0x20
00C80413  48 8B EA                        mov rbp, rdx
00C80416  0F B6 C1                        movzx eax, cl
00C80419  84 C9                           test cl, cl
00C8041B  74 22                           je 0x140c8043f
00C8041D  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00C80421  83 78 0C 00                     cmp dword ptr [rax + 0xc], 0
00C80425  7E 18                           jle 0x140c8043f
00C80427  C7 45 20 2A 00 00 00            mov dword ptr [rbp + 0x20], 0x2a
00C8042E  48 8D 15 E0 A9 FB FF            lea rdx, [rip - 0x45620]
00C80435  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00C80439  E8 02 F7 87 FF                  call 0x1404ffb40
00C8043E  90                              nop
00C8043F  48 83 C4 20                     add rsp, 0x20
00C80443  5D                              pop rbp
00C80444  C3                              ret
00C80445  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcptFinally_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 == 0) goto loc_00C8043F;
    result = *(unsigned __int64 *)(a2 + 64);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12)) >= = 0) {
        *(unsigned int *)(a2 + 32) = 42;
        a2 = v_rip - 284192;
        a1 = *(unsigned __int64 *)(a2 + 40);
        result = local_unwind(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcptFinally_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 == 0) goto loc_00C8043F;
    result = *(uint64_t *)(arg2 + 0x40);
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC)) >= = 0) {
        *(uint32_t *)(arg2 + 0x20) = 42;
        Arg2 = v_rip - 284192;
        Arg1 = *(uint64_t *)(arg2 + 0x28);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C8040D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C8040D[BB_00C8040D]
  bb_00C8041D[BB_00C8041D]
  bb_00C80427[BB_00C80427]
  bb_00C8043F[BB_00C8043F]
  bb_00C80445[BB_00C80445]
  bb_00C8040D -->|branch| bb_00C8043F
  bb_00C8040D -->|fallthrough| bb_00C8041D
  bb_00C8041D -->|branch| bb_00C8043F
  bb_00C8041D -->|fallthrough| bb_00C80427
  bb_00C80427 -->|flow| bb_00C8043F
```
