# IommuHvFlushTb

- RVA: `0x004CF9A0`–`0x004CF9D4` (길이 `52` bytes)
- VA: `0x00000001404CF9A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `16`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004CF9C7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004CF9A4` → RVA `0x00FC1D78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CF9A0  48 83 EC 38                     sub rsp, 0x38
004CF9A4  48 8B 05 CD 23 AF 00            mov rax, qword ptr [rip + 0xaf23cd]
004CF9AB  44 8B D2                        mov r10d, edx
004CF9AE  48 85 C0                        test rax, rax
004CF9B1  74 19                           je 0x1404cf9cc
004CF9B3  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
004CF9B7  4D 8B C8                        mov r9, r8
004CF9BA  45 8B C2                        mov r8d, r10d
004CF9BD  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
004CF9C2  33 C9                           xor ecx, ecx
004CF9C4  8B 52 10                        mov edx, dword ptr [rdx + 0x10]
004CF9C7  E8 04 B1 1E 00                  call 0x1406baad0
004CF9CC  33 C0                           xor eax, eax
004CF9CE  48 83 C4 38                     add rsp, 0x38
004CF9D2  C3                              ret
004CF9D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommuHvFlushTb(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = *(unsigned __int64 *)(v_rip + 11477965);
    if (*(unsigned __int64 *)(v_rip + 11477965) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 8);
        a4 = a3;
        a3 = (unsigned int)((unsigned int)(a2));
        v_stack_m18 = 0;
        a1 = 0;
        a2 = *(unsigned int *)(a2 + 16);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IommuHvFlushTb(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = *(uint64_t *)(v_rip + 0xAF23CD);
    if (*(uint64_t *)(v_rip + 0xAF23CD) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0x8);
        a4 = Arg3;
        Arg3 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m18 = 0;
        Arg1 = 0;
        Arg2 = *(uint32_t *)(Arg2 + 0x10);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CF9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CF9A0[BB_004CF9A0]
  bb_004CF9B3[BB_004CF9B3]
  bb_004CF9CC[BB_004CF9CC]
  bb_004CF9D3[BB_004CF9D3]
  bb_004CF9A0 -->|branch| bb_004CF9CC
  bb_004CF9A0 -->|fallthrough| bb_004CF9B3
  bb_004CF9B3 -->|flow| bb_004CF9CC
```
