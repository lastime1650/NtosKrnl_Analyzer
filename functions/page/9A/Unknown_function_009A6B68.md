# sub_009A6B68

- RVA: `0x009A6B68`–`0x009A6BB7` (길이 `79` bytes)
- VA: `0x00000001409A6B68`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009C8CC`
- 디코드: `15`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A6B74` → [KiGetAllocatedXSaveArea](../../text/44/KiGetAllocatedXSaveArea_function_00449950.md) (function, `0x00449950`)
- `0x009A6BAD` → [RtlXSaveS](../../text/3D/RtlXSaveS_function_003D8CE4.md) (function, `0x003D8CE4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009A6B74` → [KiGetAllocatedXSaveArea](../../text/44/KiGetAllocatedXSaveArea_function_00449950.md) (`PAGE` → `.text`)
  - `0x009A6BAD` → [RtlXSaveS](../../text/3D/RtlXSaveS_function_003D8CE4.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009A6B89` → [sub_009A6C56](Unknown_function_009A6C56.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A6B68  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
009A6B6D  4D 63 B0 E0 04 00 00            movsxd r14, dword ptr [r8 + 0x4e0]
009A6B74  E8 D7 2D AA FF                  call 0x140449950
009A6B79  48 8D 8B D0 02 00 00            lea rcx, [rbx + 0x2d0]
009A6B80  4C 8B C0                        mov r8, rax
009A6B83  49 03 CE                        add rcx, r14
009A6B86  48 85 C0                        test rax, rax
009A6B89  0F 85 C7 00 00 00               jne 0x1409a6c56
009A6B8F  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
009A6B99  48 BA 08 07 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000708
009A6BA3  48 8B 12                        mov rdx, qword ptr [rdx]
009A6BA6  48 0B 10                        or rdx, qword ptr [rax]
009A6BA9  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
009A6BAD  E8 32 21 A3 FF                  call 0x1403d8ce4
009A6BB2  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A6B68(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    unsigned __int64 v_stack_p40;

    v_stack_p40 = v_r14;
    result = KiGetAllocatedXSaveArea(a1, a2, a3, a4);
    a1 = (v_rbx + 720) + ((int)(*(unsigned int *)(a3 + 1248)));
    a2 = (*(unsigned __int64 *)(a2)) | (*(unsigned __int64 *)(result));
    a2 = (a2) & (-4);
    result = RtlXSaveS(a1, a2, result, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_009A6B68(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    uint64_t v_stack_p40;

    v_stack_p40 = local_r14;
    result = KiGetAllocatedXSaveArea(Arg1, Arg2, Arg3, Arg4);
    Arg1 = (local_rbx + 720) + ((int32_t)(*(uint32_t *)(arg3 + 0x4E0)));
    Arg2 = (*(uint64_t *)(Arg2)) | (*(uint64_t *)(result));
    Arg2 = (Arg2) & (-4);
    result = RtlXSaveS(Arg1, Arg2, result, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x4E0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A6B68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A6B68[BB_009A6B68]
  bb_009A6B8F[BB_009A6B8F]
  bb_009A6B68 -->|fallthrough| bb_009A6B8F
```
