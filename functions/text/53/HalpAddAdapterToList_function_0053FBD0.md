# HalpAddAdapterToList

- RVA: `0x0053FBD0`–`0x0053FC2C` (길이 `92` bytes)
- VA: `0x000000014053FBD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0053FBE0` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0053FC20` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [HalGetAdapterV3](../../page/70/HalGetAdapterV3_function_00709838.md) at `0x00709C23`
- [HalGetAdapterV2](../../page/70/HalGetAdapterV2_function_00709DD8.md) at `0x0070A1C2`

### Static image references
- `0x0053FBD9` → RVA `0x00FC3F30` (`.data`; read)
- `0x0053FBE5` → RVA `0x00FC3F28` (`.data`; read)
- `0x0053FBEC` → RVA `0x00FC3F20` (`.data`; read)
- `0x0053FC19` → RVA `0x00FC3F28` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053FBD0  40 53                           push rbx
0053FBD2  48 83 EC 20                     sub rsp, 0x20
0053FBD6  48 8B D9                        mov rbx, rcx
0053FBD9  48 8D 0D 50 43 A8 00            lea rcx, [rip + 0xa84350]
0053FBE0  E8 8B 88 CC FF                  call 0x140208470
0053FBE5  48 8B 0D 3C 43 A8 00            mov rcx, qword ptr [rip + 0xa8433c]
0053FBEC  48 8D 15 2D 43 A8 00            lea rdx, [rip + 0xa8432d]
0053FBF3  48 81 C3 D0 01 00 00            add rbx, 0x1d0
0053FBFA  48 39 11                        cmp qword ptr [rcx], rdx
0053FBFD  74 07                           je 0x14053fc06
0053FBFF  B9 03 00 00 00                  mov ecx, 3
0053FC04  CD 29                           int 0x29
0053FC06  48 89 13                        mov qword ptr [rbx], rdx
0053FC09  8A D0                           mov dl, al
0053FC0B  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
0053FC0F  48 89 19                        mov qword ptr [rcx], rbx
0053FC12  48 8D 0D 17 43 A8 00            lea rcx, [rip + 0xa84317]
0053FC19  48 89 1D 08 43 A8 00            mov qword ptr [rip + 0xa84308], rbx
0053FC20  E8 7B 2F E5 FF                  call 0x140392ba0
0053FC25  48 83 C4 20                     add rsp, 0x20
0053FC29  5B                              pop rbx
0053FC2A  C3                              ret
0053FC2B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAddAdapterToList(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11027280, a2, a3, a4);
    v_rbx = (a1) + (464);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027260))) != (v_rip + 11027245)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_rbx) = v_rip + 11027245;
    *(unsigned __int64 *)(v_rbx + 8) = a1;
    *(unsigned __int64 *)(a1) = v_rbx;
    *(unsigned __int64 *)(v_rip + 11027208) = v_rbx;
    result = KeReleaseSpinLock(v_rip + 11027223, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpAddAdapterToList(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11027280, a2, a3, a4);
    local_rbx = (Arg1) + (464);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA8433C))) != (v_rip + 11027245)) {
        Arg1 = 3;
    }
    *(uint64_t *)(local_rbx) = v_rip + 11027245;
    *(void **)(local_rbx + 0x8) = Arg1;
    *(uint64_t *)(arg1) = local_rbx;
    *(uint64_t *)(v_rip + 0xA84308) = local_rbx;
    result = KeReleaseSpinLock(v_rip + 11027223, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053FBD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053FBD0[BB_0053FBD0]
  bb_0053FBFF[BB_0053FBFF]
  bb_0053FC06[BB_0053FC06]
  bb_0053FC2B[BB_0053FC2B]
  bb_0053FBD0 -->|branch| bb_0053FC06
  bb_0053FBD0 -->|fallthrough| bb_0053FBFF
  bb_0053FBFF -->|flow| bb_0053FC06
```
