# IommuHvGetConfiguration

- RVA: `0x00C24FD0`–`0x00C2501E` (길이 `78` bytes)
- VA: `0x0000000140C24FD0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `25`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00C25003` → [IommupGetSystemContext](../../text/56/IommupGetSystemContext_function_00566310.md) (function, `0x00566310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C24FDB` → RVA `0x00F8FAD4` (`.data`; read)
- `0x00C24FF2` → RVA `0x00F8FAD8` (`.data`; read)
- `0x00C24FFA` → RVA `0x00F8FAF0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C25003` → [IommupGetSystemContext](../../text/56/IommupGetSystemContext_function_00566310.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C24FD0  40 53                           push rbx
00C24FD2  48 83 EC 20                     sub rsp, 0x20
00C24FD6  33 C0                           xor eax, eax
00C24FD8  49 8B D9                        mov rbx, r9
00C24FDB  38 05 F3 AA 36 00               cmp byte ptr [rip + 0x36aaf3], al
00C24FE1  75 0F                           jne 0x140c24ff2
00C24FE3  89 02                           mov dword ptr [rdx], eax
00C24FE5  41 89 00                        mov dword ptr [r8], eax
00C24FE8  49 89 01                        mov qword ptr [r9], rax
00C24FEB  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00C24FF0  EB 25                           jmp 0x140c25017
00C24FF2  8B 05 E0 AA 36 00               mov eax, dword ptr [rip + 0x36aae0]
00C24FF8  89 02                           mov dword ptr [rdx], eax
00C24FFA  8B 05 F0 AA 36 00               mov eax, dword ptr [rip + 0x36aaf0]
00C25000  41 89 00                        mov dword ptr [r8], eax
00C25003  E8 08 13 94 FF                  call 0x140566310
00C25008  48 89 03                        mov qword ptr [rbx], rax
00C2500B  48 F7 D8                        neg rax
00C2500E  1B C0                           sbb eax, eax
00C25010  F7 D0                           not eax
00C25012  25 9A 00 00 C0                  and eax, 0xc000009a
00C25017  48 83 C4 20                     add rsp, 0x20
00C2501B  5B                              pop rbx
00C2501C  C3                              ret
00C2501D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommuHvGetConfiguration(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 0;
    if ((*(unsigned __int8 *)(v_rip + 3582707)) != 0) goto loc_00C24FF2;
    *(unsigned int *)(a2) = 0;
    *(unsigned int *)(a3) = 0;
    *(unsigned __int64 *)(a4) = 0;
    goto loc_00C25017;
loc_00C24FF2:
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3582688)));
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3582704)));
    result = IommupGetSystemContext(a1, a2, a3, a4);
    *(unsigned __int64 *)(a4) = result;
    result = -(result);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC000009AULL));
loc_00C25017:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IommuHvGetConfiguration(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 0;
    if ((*(uint8_t *)(v_rip + 0x36AAF3)) != 0) goto loc_00C24FF2;
    *(uint32_t *)(arg2) = 0;
    *(uint32_t *)(arg3) = 0;
    *(uint64_t *)(arg4) = 0;
    goto loc_00C25017;
loc_00C24FF2:
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x36AAE0)));
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x36AAF0)));
    result = IommupGetSystemContext(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(arg4) = result;
    result = -(result);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC000009AULL));
loc_00C25017:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C24FD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C24FD0[BB_00C24FD0]
  bb_00C24FE3[BB_00C24FE3]
  bb_00C24FF2[BB_00C24FF2]
  bb_00C25017[BB_00C25017]
  bb_00C2501D[BB_00C2501D]
  bb_00C24FD0 -->|branch| bb_00C24FF2
  bb_00C24FD0 -->|fallthrough| bb_00C24FE3
  bb_00C24FE3 -->|branch| bb_00C25017
  bb_00C24FF2 -->|flow| bb_00C25017
```
