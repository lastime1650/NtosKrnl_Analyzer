# PnpTraceStartDevice

- RVA: `0x0026E3F8`–`0x0026E477` (길이 `127` bytes)
- VA: `0x000000014026E3F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006570C`
- 디코드: `37`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0026E42D` → [PnpDiagnosticTraceDeviceOperation](PnpDiagnosticTraceDeviceOperation_function_0026E1B8.md) (function, `0x0026E1B8`)
- `0x0026E45E` → [RtlImageNtHeaderEx](../41/RtlImageNtHeaderEx_function_0041EAA0.md) (function, `0x0041EAA0`)

### Direct callers
- [PnpDeviceCompletionRoutine](PnpDeviceCompletionRoutine_function_0026E6C0.md) at `0x0026E76B`
- [PnpStartDeviceNode](../../page/8F/PnpStartDeviceNode_function_008FE38C.md) at `0x008FE47B`

### Static image references
- `0x0026E420` → RVA `0x00010870` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0026E3F8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0026E3FD  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0026E402  57                              push rdi
0026E403  48 83 EC 30                     sub rsp, 0x30
0026E407  48 8B F1                        mov rsi, rcx
0026E40A  49 8B C0                        mov rax, r8
0026E40D  33 C9                           xor ecx, ecx
0026E40F  8B FA                           mov edi, edx
0026E411  8B D9                           mov ebx, ecx
0026E413  4D 85 C0                        test r8, r8
0026E416  75 2D                           jne 0x14026e445
0026E418  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0026E41C  48 8D 56 28                     lea rdx, [rsi + 0x28]
0026E420  48 8D 0D 49 24 DA FF            lea rcx, [rip - 0x25dbb7]
0026E427  4C 8B CB                        mov r9, rbx
0026E42A  44 8B C7                        mov r8d, edi
0026E42D  E8 86 FD FF FF                  call 0x14026e1b8
0026E432  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0026E437  33 C0                           xor eax, eax
0026E439  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0026E43E  48 83 C4 30                     add rsp, 0x30
0026E442  5F                              pop rdi
0026E443  C3                              ret
0026E444  CC                              int3
0026E445  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
0026E449  49 8D 58 38                     lea rbx, [r8 + 0x38]
0026E44D  45 33 C0                        xor r8d, r8d
0026E450  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0026E455  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
0026E45A  41 8D 48 01                     lea ecx, [r8 + 1]
0026E45E  E8 3D 06 1B 00                  call 0x14041eaa0
0026E463  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0026E468  0F B7 48 44                     movzx ecx, word ptr [rax + 0x44]
0026E46C  0F B7 40 46                     movzx eax, word ptr [rax + 0x46]
0026E470  C1 E1 10                        shl ecx, 0x10
0026E473  0B C8                           or ecx, eax
0026E475  EB A1                           jmp 0x14026e418
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpTraceStartDevice(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p40;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a1 = 0;
    if (a3 != 0) goto loc_0026E445;
loc_0026E418:
    v_stack_m18 = 0;
    result = PnpDiagnosticTraceDeviceOperation(v_rip - 2481079, a1 + 40, (unsigned int)((unsigned int)((unsigned int)(a2))), 0);
    result = 0;
    v_rsp = (v_rsp) + (48);
    return result;
loc_0026E445:
    a3 = 0;
    v_stack_p40 = v_rip - 2481079;
    result = RtlImageNtHeaderEx(a3 + 1, *(unsigned __int64 *)(result + 24), a3, v_stack_p40);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p40 + 68)) << (16));
    a1 = (unsigned int)((a1) | ((unsigned int)(*(unsigned __int16 *)(v_stack_p40 + 70))));
    goto loc_0026E418;
}
```

## 5. (Beta) C Style

```c
int64_t PnpTraceStartDevice(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p40;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg1 = 0;
    if (Arg3 != NULL) goto loc_0026E445;
loc_0026E418:
    v_stack_m18 = 0;
    result = PnpDiagnosticTraceDeviceOperation(v_rip - 2481079, Arg1 + 40, (uint32_t)((uint32_t)((uint32_t)(Arg2))), 0);
    result = 0;
    local_rsp = (local_rsp) + (48);
    return result;
loc_0026E445:
    Arg3 = 0;
    v_stack_p40 = v_rip - 2481079;
    result = RtlImageNtHeaderEx(Arg3 + 1, *(uint64_t *)(result + 0x18), Arg3, v_stack_p40);
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p40 + 0x44)) << (16));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(*(uint16_t *)(v_stack_p40 + 0x46))));
    goto loc_0026E418;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026E3F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0026E3F8[BB_0026E3F8]
  bb_0026E418[BB_0026E418]
  bb_0026E444[BB_0026E444]
  bb_0026E445[BB_0026E445]
  bb_0026E3F8 -->|branch| bb_0026E445
  bb_0026E3F8 -->|fallthrough| bb_0026E418
  bb_0026E444 -->|flow| bb_0026E445
  bb_0026E445 -->|branch| bb_0026E418
```
