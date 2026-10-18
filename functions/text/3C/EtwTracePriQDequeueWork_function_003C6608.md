# EtwTracePriQDequeueWork

- RVA: `0x003C6608`–`0x003C6688` (길이 `128` bytes)
- VA: `0x00000001403C6608`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E540`
- 디코드: `28`개 명령, `128/128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003C6632` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003C6681` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- [KeRemovePriQueue](KeRemovePriQueue_function_003C5090.md) at `0x003C543D`
- [KeRemovePriQueue](KeRemovePriQueue_function_003C5090.md) at `0x003C5634`

### Static image references
- `0x003C660C` → RVA `0x00E0A740` (`.data`; read)
- `0x003C6620` → RVA `0x00FC6B1C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C6608  48 83 EC 68                     sub rsp, 0x68
003C660C  48 8B 05 2D 41 A4 00            mov rax, qword ptr [rip + 0xa4412d]
003C6613  48 33 C4                        xor rax, rsp
003C6616  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003C661B  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
003C6620  8B 05 F6 04 C0 00               mov eax, dword ptr [rip + 0xc004f6]
003C6626  A8 08                           test al, 8
003C6628  74 13                           je 0x1403c663d
003C662A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003C662F  48 33 CC                        xor rcx, rsp
003C6632  E8 09 60 2E 00                  call 0x1406ac640
003C6637  48 83 C4 68                     add rsp, 0x68
003C663B  C3                              ret
003C663C  CC                              int3
003C663D  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
003C6643  41 B9 51 05 00 00               mov r9d, 0x551
003C6649  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
003C664E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
003C6653  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
003C6657  41 B8 00 00 00 21               mov r8d, 0x21000000
003C665D  48 8D 44 24 30                  lea rax, [rsp + 0x30]
003C6662  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003C6667  BA 01 00 00 00                  mov edx, 1
003C666C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003C6671  C7 44 24 48 0C 00 00 00         mov dword ptr [rsp + 0x48], 0xc
003C6679  C7 44 24 20 02 1E 60 01         mov dword ptr [rsp + 0x20], 0x1601e02
003C6681  E8 CA EC E6 FF                  call 0x140235350
003C6686  EB A2                           jmp 0x1403c662a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTracePriQDequeueWork(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m2C;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 10764589)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12584182)))) & (8)) == 0) goto loc_003C663D;
loc_003C662A:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
loc_003C663D:
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1296)));
    v_stack_p30 = a2;
    v_stack_p40 = v_stack_p30;
    v_stack_p48 = 12;
    v_stack_p20 = 0x1601E02ULL;
    result = EtwTraceKernelEvent(v_stack_p40, 1, (unsigned int)(0x21000000ULL), (unsigned int)(0x551ULL));
    goto loc_003C662A;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTracePriQDequeueWork(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m2C;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0xA4412D)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC004F6)))) & (8)) == 0) goto loc_003C663D;
loc_003C662A:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
loc_003C663D:
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x510)));
    v_stack_p30 = Arg2;
    v_stack_p40 = v_stack_p30;
    v_stack_p48 = 12;
    v_stack_p20 = 0x1601E02ULL;
    result = EtwTraceKernelEvent(v_stack_p40, 1, (uint32_t)(0x21000000ULL), (uint32_t)(0x551ULL));
    goto loc_003C662A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x510` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C6608&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C6608[BB_003C6608]
  bb_003C662A[BB_003C662A]
  bb_003C663C[BB_003C663C]
  bb_003C663D[BB_003C663D]
  bb_003C6608 -->|branch| bb_003C663D
  bb_003C6608 -->|fallthrough| bb_003C662A
  bb_003C663C -->|flow| bb_003C663D
  bb_003C663D -->|branch| bb_003C662A
```
