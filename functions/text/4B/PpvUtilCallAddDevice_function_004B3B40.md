# PpvUtilCallAddDevice

- RVA: `0x004B3B40`–`0x004B3BB8` (길이 `120` bytes)
- VA: `0x00000001404B3B40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9AD0`
- 디코드: `35`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B3B72` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004B3B8D` → [VfDevObjPreAddDevice](../../pagevrfy/BB/VfDevObjPreAddDevice_function_00BB963C.md) (function, `0x00BB963C`)
- `0x004B3B9B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004B3BAF` → [VfDevObjPostAddDevice](../../pagevrfy/BB/VfDevObjPostAddDevice_function_00BB9688.md) (function, `0x00BB9688`)

### Direct callers
- [PnpCallAddDevice](../../page/8F/PnpCallAddDevice_function_008FC164.md) at `0x008FC1FB`

### Static image references
- `0x004B3B54` → RVA `0x00E663C8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004B3B8D` → [VfDevObjPreAddDevice](../../pagevrfy/BB/VfDevObjPreAddDevice_function_00BB963C.md) (`.text` → `PAGEVRFY`)
  - `0x004B3BAF` → [VfDevObjPostAddDevice](../../pagevrfy/BB/VfDevObjPostAddDevice_function_00BB9688.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B3B40  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004B3B45  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
004B3B4A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
004B3B4F  57                              push rdi
004B3B50  48 83 EC 30                     sub rsp, 0x30
004B3B54  80 3D 6D 28 9B 00 00            cmp byte ptr [rip + 0x9b286d], 0
004B3B5B  41 8B E9                        mov ebp, r9d
004B3B5E  49 8B D8                        mov rbx, r8
004B3B61  48 8B FA                        mov rdi, rdx
004B3B64  48 8B F1                        mov rsi, rcx
004B3B67  75 24                           jne 0x1404b3b8d
004B3B69  48 8B D1                        mov rdx, rcx
004B3B6C  48 8B C3                        mov rax, rbx
004B3B6F  48 8B CF                        mov rcx, rdi
004B3B72  E8 59 6F 20 00                  call 0x1406baad0
004B3B77  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
004B3B7C  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
004B3B81  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
004B3B86  48 83 C4 30                     add rsp, 0x30
004B3B8A  5F                              pop rdi
004B3B8B  C3                              ret
004B3B8C  CC                              int3
004B3B8D  E8 AA 5A 70 00                  call 0x140bb963c
004B3B92  48 8B D6                        mov rdx, rsi
004B3B95  48 8B CF                        mov rcx, rdi
004B3B98  48 8B C3                        mov rax, rbx
004B3B9B  E8 30 6F 20 00                  call 0x1406baad0
004B3BA0  44 8B CD                        mov r9d, ebp
004B3BA3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004B3BA7  48 8B D7                        mov rdx, rdi
004B3BAA  48 8B CE                        mov rcx, rsi
004B3BAD  8B D8                           mov ebx, eax
004B3BAF  E8 D4 5A 70 00                  call 0x140bb9688
004B3BB4  8B C3                           mov eax, ebx
004B3BB6  EB BF                           jmp 0x1404b3b77
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpvUtilCallAddDevice(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int8 *)(v_rip + 10168429)) != 0) goto loc_004B3B8D;
    result = guard_dispatch_icall(a2, a1, a3, a4);
loc_004B3B77:
    v_rsp = (v_rsp) + (48);
    return result;
loc_004B3B8D:
    result = VfDevObjPreAddDevice(a2, a1, a3, a4);
    result = guard_dispatch_icall(a2, v_stack_p18, a3, a4);
    v_stack_p20 = (unsigned int)(result);
    result = VfDevObjPostAddDevice(v_stack_p18, a2, a3, (unsigned int)((unsigned int)(v_stack_p10)));
    goto loc_004B3B77;
}
```

## 5. (Beta) C Style

```c
int64_t PpvUtilCallAddDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    if ((*(uint8_t *)(v_rip + 0x9B286D)) != 0) goto loc_004B3B8D;
    result = guard_dispatch_icall(Arg2, Arg1, Arg3, Arg4);
loc_004B3B77:
    local_rsp = (local_rsp) + (48);
    return result;
loc_004B3B8D:
    result = VfDevObjPreAddDevice(Arg2, Arg1, Arg3, Arg4);
    result = guard_dispatch_icall(Arg2, v_stack_p18, Arg3, Arg4);
    v_stack_p20 = (uint32_t)(result);
    result = VfDevObjPostAddDevice(v_stack_p18, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_p10)));
    goto loc_004B3B77;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B3B40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B3B40[BB_004B3B40]
  bb_004B3B69[BB_004B3B69]
  bb_004B3B77[BB_004B3B77]
  bb_004B3B8C[BB_004B3B8C]
  bb_004B3B8D[BB_004B3B8D]
  bb_004B3B40 -->|branch| bb_004B3B8D
  bb_004B3B40 -->|fallthrough| bb_004B3B69
  bb_004B3B69 -->|flow| bb_004B3B77
  bb_004B3B8C -->|flow| bb_004B3B8D
  bb_004B3B8D -->|branch| bb_004B3B77
```
