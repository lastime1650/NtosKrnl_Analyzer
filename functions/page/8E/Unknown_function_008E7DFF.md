# sub_008E7DFF

- RVA: `0x008E7DFF`–`0x008E7E6F` (길이 `112` bytes)
- VA: `0x00000001408E7DFF`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086914`
- 디코드: `27`개 명령, `112/112` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008E7E58` → [PiCMCaptureObjectInputData](PiCMCaptureObjectInputData_function_008E8220.md) (function, `0x008E8220`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008E7E69` → [sub_008E802B + 0x1F](Unknown_function_008E802B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E7DFF  49 89 6B 08                     mov qword ptr [r11 + 8], rbp
008E7E03  0F 57 C0                        xorps xmm0, xmm0
008E7E06  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
008E7E0A  33 C0                           xor eax, eax
008E7E0C  4D 89 63 F0                     mov qword ptr [r11 - 0x10], r12
008E7E10  49 8B F8                        mov rdi, r8
008E7E13  45 33 C0                        xor r8d, r8d
008E7E16  4D 89 6B E8                     mov qword ptr [r11 - 0x18], r13
008E7E1A  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
008E7E1F  4D 89 73 E0                     mov qword ptr [r11 - 0x20], r14
008E7E23  45 8B E9                        mov r13d, r9d
008E7E26  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
008E7E2A  4D 8D 4B B0                     lea r9, [r11 - 0x50]
008E7E2E  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
008E7E36  41 8B E8                        mov ebp, r8d
008E7E39  45 8B E0                        mov r12d, r8d
008E7E3C  4D 89 7B D8                     mov qword ptr [r11 - 0x28], r15
008E7E40  45 8B F0                        mov r14d, r8d
008E7E43  41 0F 11 43 C0                  movups xmmword ptr [r11 - 0x40], xmm0
008E7E48  44 89 00                        mov dword ptr [rax], r8d
008E7E4B  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
008E7E53  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
008E7E58  E8 C3 03 00 00                  call 0x1408e8220
008E7E5D  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
008E7E65  8B D8                           mov ebx, eax
008E7E67  85 C0                           test eax, eax
008E7E69  0F 88 DB 01 00 00               js 0x1408e804a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E7DFF(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, unsigned int a30, __int64 a31)
{
    __int64 result;

    *(unsigned __int64 *)(v_r11 + 8) = v_rbp;
    *(unsigned __int64 *)(v_r11 + 32) = v_rdi;
    result = 0;
    *(unsigned __int64 *)(v_r11 - 16) = v_r12;
    a3 = 0;
    *(unsigned __int64 *)(v_r11 - 24) = v_r13;
    a15 = v_xmm0;
    *(unsigned __int64 *)(v_r11 - 32) = v_r14;
    *(unsigned __int64 *)(v_r11 - 48) = 0;
    *(unsigned __int64 *)(v_r11 - 40) = v_r15;
    *(unsigned __int64 *)(v_r11 - 64) = v_xmm0;
    *(unsigned int *)(a31) = 0;
    a13 = v_xmm0;
    result = PiCMCaptureObjectInputData(a1, a2, (unsigned int)(a30), v_r11 - 80);
}
```

## 5. (Beta) C Style

```c
int64_t sub_008E7DFF(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13, uint64_t Arg14, int64_t Arg15, uint64_t Arg16, int64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint32_t Arg30, void *Arg31)
{
    uint8_t *arg31 = (uint8_t *)Arg31;

    int64_t result;

    *(uint64_t *)(local_r11 + 0x8) = local_rbp;
    *(uint64_t *)(local_r11 + 0x20) = local_rdi;
    result = 0;
    *(uint64_t *)(local_r11 - 0x10) = local_r12;
    Arg3 = 0;
    *(uint64_t *)(local_r11 - 0x18) = local_r13;
    Arg15 = v_xmm0;
    *(uint64_t *)(local_r11 - 0x20) = local_r14;
    *(uint64_t *)(local_r11 - 0x30) = 0;
    *(uint64_t *)(local_r11 - 0x28) = local_r15;
    *(uint64_t *)(local_r11 - 0x40) = v_xmm0;
    *(uint32_t *)(arg31) = 0;
    Arg13 = v_xmm0;
    result = PiCMCaptureObjectInputData(Arg1, Arg2, (uint32_t)(Arg30), local_r11 - 80);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg31` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E7DFF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E7DFF[BB_008E7DFF]
```
