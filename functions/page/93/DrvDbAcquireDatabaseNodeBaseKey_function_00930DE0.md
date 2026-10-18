# DrvDbAcquireDatabaseNodeBaseKey

- RVA: `0x00930DE0`–`0x00930E38` (길이 `88` bytes)
- VA: `0x0000000140930DE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EBD8`
- 디코드: `25`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00930E28` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)

### Direct callers
- [DrvDbDeleteObjectRegKey](../83/DrvDbDeleteObjectRegKey_function_00832D70.md) at `0x00832DDD`
- [DrvDbDeleteObjectRegKey](../83/DrvDbDeleteObjectRegKey_function_00832D70.md) at `0x00832E42`
- [DrvDbGetObjectList](../92/DrvDbGetObjectList_function_0092F224.md) at `0x0092F2EF`
- [DrvDbGetObjectList](../92/DrvDbGetObjectList_function_0092F224.md) at `0x0092F395`
- [sub_0093107C](Unknown_function_0093107C.md) at `0x00931285`
- [sub_00931420](Unknown_function_00931420.md) at `0x009314CD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00930E28` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00930E32` → [sub_00930F36](Unknown_function_00930F36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00930DE0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00930DE5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00930DEA  56                              push rsi
00930DEB  57                              push rdi
00930DEC  41 54                           push r12
00930DEE  41 56                           push r14
00930DF0  41 57                           push r15
00930DF2  48 83 EC 50                     sub rsp, 0x50
00930DF6  45 33 FF                        xor r15d, r15d
00930DF9  49 63 E8                        movsxd rbp, r8d
00930DFC  4D 89 39                        mov qword ptr [r9], r15
00930DFF  48 8B FA                        mov rdi, rdx
00930E02  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00930E0B  4C 8B E1                        mov r12, rcx
00930E0E  B2 01                           mov dl, 1
00930E10  4D 8B F1                        mov r14, r9
00930E13  41 8B DF                        mov ebx, r15d
00930E16  41 8B F7                        mov esi, r15d
00930E19  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00930E20  90                              nop
00930E21  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
00930E28  E8 F3 3F 8E FF                  call 0x140214e20
00930E2D  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
00930E30  A8 04                           test al, 4
00930E32  0F 85 FE 00 00 00               jne 0x140930f36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbAcquireDatabaseNodeBaseKey(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (80);
    v_r15 = 0;
    *(unsigned __int64 *)(a4) = 0;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(a2 + 152), 1, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbAcquireDatabaseNodeBaseKey(int64_t Arg1, void *Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (80);
    local_r15 = 0;
    *(uint64_t *)(arg4) = 0;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(arg2 + 0x98), 1, Arg3, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x98` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00930DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00930DE0[BB_00930DE0]
```
