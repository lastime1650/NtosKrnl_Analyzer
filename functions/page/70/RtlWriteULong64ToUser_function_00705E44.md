# RtlWriteULong64ToUser

- RVA: `0x00705E44`–`0x00705E84` (길이 `64` bytes)
- VA: `0x0000000140705E44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00705E60` → `indirect target` (indirect, 간접 대상)
- `0x00705E70` → [ProbeForRead](../9C/ProbeForRead_function_009C5130.md) (function, `0x009C5130`)

### Direct callers
- [PspCopyUserAttributes](../78/PspCopyUserAttributes_function_00784234.md) at `0x007842E0`
- [PspCopyAndFixupParameters](../AE/PspCopyAndFixupParameters_function_00AEB878.md) at `0x00AEBBBF`
- [PspCopyAndFixupParameters](../AE/PspCopyAndFixupParameters_function_00AEB878.md) at `0x00AEBC7A`

### Static image references
- `0x00705E4E` → RVA `0x001517F0` (`.idata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705E44  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00705E49  57                              push rdi
00705E4A  48 83 EC 20                     sub rsp, 0x20
00705E4E  48 8B 05 9B B9 A4 FF            mov rax, qword ptr [rip - 0x5b4665]
00705E55  48 8B FA                        mov rdi, rdx
00705E58  48 8B D9                        mov rbx, rcx
00705E5B  48 85 C0                        test rax, rax
00705E5E  74 07                           je 0x140705e67
00705E60  FF D0                           call rax
00705E62  0F 1F 00                        nop dword ptr [rax]
00705E65  EB 11                           jmp 0x140705e78
00705E67  BA 08 00 00 00                  mov edx, 8
00705E6C  44 8D 42 F9                     lea r8d, [rdx - 7]
00705E70  E8 BB F2 2B 00                  call 0x1409c5130
00705E75  48 89 3B                        mov qword ptr [rbx], rdi
00705E78  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00705E7D  48 83 C4 20                     add rsp, 0x20
00705E81  5F                              pop rdi
00705E82  C3                              ret
00705E83  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlWriteULong64ToUser(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(v_rip - 5981797) == 0) goto loc_00705E67;
    result = kernel_indirect_call(a1, a2, a3, a4);
    goto loc_00705E78;
loc_00705E67:
    result = ProbeForRead(a1, 8, 8 - 7, a4);
    *(unsigned __int64 *)(a1) = a2;
loc_00705E78:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlWriteULong64ToUser(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(v_rip - 0x5B4665) == 0) goto loc_00705E67;
    result = kernel_indirect_call(Arg1, Arg2, a3, a4);
    goto loc_00705E78;
loc_00705E67:
    result = ProbeForRead(Arg1, 8, 8 - 7, a4);
    *(uint64_t *)(arg1) = Arg2;
loc_00705E78:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705E44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705E44[BB_00705E44]
  bb_00705E60[BB_00705E60]
  bb_00705E67[BB_00705E67]
  bb_00705E78[BB_00705E78]
  bb_00705E83[BB_00705E83]
  bb_00705E44 -->|branch| bb_00705E67
  bb_00705E44 -->|fallthrough| bb_00705E60
  bb_00705E60 -->|branch| bb_00705E78
  bb_00705E67 -->|flow| bb_00705E78
```
