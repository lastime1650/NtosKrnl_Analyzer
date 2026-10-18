# PiSwIrpInterfacePropertySet$filt$0

- RVA: `0x00B0F0CC`–`0x00B0F0EE` (길이 `34` bytes)
- VA: `0x0000000140B0F0CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00087AD4`
- 디코드: `12`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B0F0DA` → `msrpc.sys!RpcExceptionFilter` (import, 간접 대상; import `msrpc.sys!RpcExceptionFilter`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B0F0DA` → RVA `0x001516D8` (`msrpc.sys!RpcExceptionFilter (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0F0CC  40 55                           push rbp
00B0F0CE  48 83 EC 30                     sub rsp, 0x30
00B0F0D2  48 8B EA                        mov rbp, rdx
00B0F0D5  48 8B 01                        mov rax, qword ptr [rcx]
00B0F0D8  8B 08                           mov ecx, dword ptr [rax]
00B0F0DA  48 FF 15 F7 25 64 FF            call qword ptr [rip - 0x9bda09]
00B0F0E1  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B0F0E6  90                              nop
00B0F0E7  48 83 C4 30                     add rsp, 0x30
00B0F0EB  5D                              pop rbp
00B0F0EC  C3                              ret
00B0F0ED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwIrpInterfacePropertySet_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = msrpc_sys_RpcExceptionFilter((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))), a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwIrpInterfacePropertySet_filt_0(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = kernel_indirect_call((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))), Arg2, a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0F0CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0F0CC[BB_00B0F0CC]
  bb_00B0F0ED[BB_00B0F0ED]
```
