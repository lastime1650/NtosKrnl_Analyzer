# VerifierIoVolumeDeviceToDosName

- RVA: `0x00BA2180`–`0x00BA21ED` (길이 `109` bytes)
- VA: `0x0000000140BA2180`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065960`
- 디코드: `29`개 명령, `109/109` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00BA21CA` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)
- `0x00BA21DC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BA218A` → RVA `0x00F04A20` (`.data`; read)
- `0x00BA21CF` → RVA `0x00FFE170` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA21DC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA2180  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BA2185  57                              push rdi
00BA2186  48 83 EC 40                     sub rsp, 0x40
00BA218A  8B 05 90 28 36 00               mov eax, dword ptr [rip + 0x362890]
00BA2190  48 8B DA                        mov rbx, rdx
00BA2193  48 8B F9                        mov rdi, rcx
00BA2196  A8 10                           test al, 0x10
00BA2198  74 35                           je 0x140ba21cf
00BA219A  45 0F 20 C0                     mov r8, cr8
00BA219E  45 84 C0                        test r8b, r8b
00BA21A1  74 2C                           je 0x140ba21cf
00BA21A3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BA21A8  BA E5 00 00 00                  mov edx, 0xe5
00BA21AD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BA21B2  45 33 C9                        xor r9d, r9d
00BA21B5  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00BA21BD  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BA21C3  8D 4A DF                        lea ecx, [rdx - 0x21]
00BA21C6  45 0F B6 C0                     movzx r8d, r8b
00BA21CA  E8 35 B7 FF FF                  call 0x140b9d904
00BA21CF  48 8B 05 9A BF 45 00            mov rax, qword ptr [rip + 0x45bf9a]
00BA21D6  48 8B D3                        mov rdx, rbx
00BA21D9  48 8B CF                        mov rcx, rdi
00BA21DC  E8 EF 88 B1 FF                  call 0x1406baad0
00BA21E1  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00BA21E6  48 83 C4 40                     add rsp, 0x40
00BA21EA  5F                              pop rdi
00BA21EB  C3                              ret
00BA21EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierIoVolumeDeviceToDosName(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3549328)))) & (16)) == 0) goto loc_00BA21CF;
    result = (unsigned int)(*(unsigned int *)(v_rip + 3549328));
    if ((unsigned __int8)(v_cr8) != 0) {
        result = v_stack_p0;
        a2 = 229;
        v_stack_m18 = result;
        a4 = 0;
        v_stack_m20 = 4;
        a1 = a2 - 33;
        a3 = (unsigned __int8)(v_cr8);
        result = CarReportRuleViolationFromNt(a1, a2, a3, a4);
    }
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierIoVolumeDeviceToDosName(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x362890)))) & (16)) == 0) goto loc_00BA21CF;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x362890));
    if ((uint8_t)(v_cr8) != 0) {
        result = v_stack_p0;
        Arg2 = 229;
        v_stack_m18 = result;
        Arg4 = 0;
        v_stack_m20 = 4;
        Arg1 = Arg2 - 33;
        Arg3 = (uint8_t)(v_cr8);
        result = CarReportRuleViolationFromNt(Arg1, Arg2, Arg3, Arg4);
    }
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA2180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA2180[BB_00BA2180]
  bb_00BA219A[BB_00BA219A]
  bb_00BA21A3[BB_00BA21A3]
  bb_00BA21CF[BB_00BA21CF]
  bb_00BA21EC[BB_00BA21EC]
  bb_00BA2180 -->|branch| bb_00BA21CF
  bb_00BA2180 -->|fallthrough| bb_00BA219A
  bb_00BA219A -->|branch| bb_00BA21CF
  bb_00BA219A -->|fallthrough| bb_00BA21A3
  bb_00BA21A3 -->|flow| bb_00BA21CF
```
